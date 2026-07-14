from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'locations'
        ordering = ['name']

    def __str__(self):
        return self.name


class AssetManager(models.Manager):
    def active(self):
        return self.filter(status=Asset.Status.ACTIVE)

    def expiring_soon(self, days=30):
        from django.utils import timezone
        from datetime import timedelta
        threshold = timezone.now().date() + timedelta(days=days)
        return self.filter(
            vendor_contract_end__isnull=False,
            vendor_contract_end__lte=threshold,
            vendor_contract_end__gte=timezone.now().date()
        )

    def expired(self):
        from django.utils import timezone
        return self.filter(
            vendor_contract_end__isnull=False,
            vendor_contract_end__lt=timezone.now().date()
        )


class Asset(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Aktif'
        MAINTENANCE = 'maintenance', 'Perbaikan'
        DECOMMISSIONED = 'decommissioned', 'Dihapus'

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='assets')
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=200, blank=True)
    serial_number = models.CharField(max_length=200, unique=True)
    asset_number = models.CharField(max_length=100, unique=True)
    office_version = models.CharField(max_length=100, blank=True)
    email_license_status = models.CharField(max_length=100, blank=True)
    user_pc = models.CharField(max_length=200, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='assets')
    acquisition_date = models.DateField()
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0'))])
    vendor_name = models.CharField(max_length=200, blank=True)
    vendor_contract_end = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    objects = AssetManager()

    class Meta:
        db_table = 'assets'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['serial_number']),
            models.Index(fields=['asset_number']),
            models.Index(fields=['category', 'status']),
            models.Index(fields=['vendor_contract_end']),
        ]

    def __str__(self):
        return f"{self.brand} - {self.serial_number}"

    def is_contract_expiring(self, days=30):
        if not self.vendor_contract_end:
            return False
        from django.utils import timezone
        from datetime import timedelta
        remaining = self.vendor_contract_end - timezone.now().date()
        return 0 <= remaining.days <= days

    def is_contract_expired(self):
        if not self.vendor_contract_end:
            return False
        from django.utils import timezone
        return self.vendor_contract_end < timezone.now().date()


class PhysicalAsset(models.Model):
    asset_name = models.CharField(max_length=200)
    sub_class = models.CharField(max_length=150, db_index=True)
    operating_system = models.CharField(max_length=200, blank=True)
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=150, blank=True, db_index=True)
    serial_number = models.CharField(max_length=150, db_index=True)
    owner = models.CharField(max_length=200, db_index=True)
    location = models.CharField(max_length=200, db_index=True)
    asset_number = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    confidentiality = models.SmallIntegerField(null=True, blank=True)
    integrity = models.SmallIntegerField(null=True, blank=True)
    availability = models.SmallIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='asset_images/', null=True, blank=True)
    import_month = models.CharField(max_length=7, default="2026-07", db_index=True)
    technical_specs = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'physical_assets'
        ordering = ['asset_name']
        indexes = [
            models.Index(fields=['serial_number']),
            models.Index(fields=['asset_number']),
            models.Index(fields=['import_month']),
        ]

    def __str__(self):
        return f"{self.asset_name} ({self.serial_number})"


class SoftwareLicense(models.Model):
    name = models.CharField(max_length=300)
    license_type = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=300, blank=True)
    license_number = models.CharField(max_length=500, blank=True)
    quantity = models.CharField(max_length=50, blank=True)
    location_install = models.CharField(max_length=300, blank=True)
    room_location = models.CharField(max_length=200, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    import_month = models.CharField(max_length=7, default="2026-07", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'software_licenses'
        ordering = ['name']
        indexes = [
            models.Index(fields=['license_type']),
            models.Index(fields=['vendor']),
            models.Index(fields=['status']),
            models.Index(fields=['import_month']),
        ]

    def __str__(self):
        return f"{self.name}"


class NotebookLeaseQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=self.model.Status.ACTIVE)

    def expiring_soon(self, days=30):
        from django.utils import timezone
        from datetime import timedelta
        threshold = timezone.now().date() + timedelta(days=days)
        return self.filter(
            contract_end__isnull=False,
            contract_end__lte=threshold,
            contract_end__gte=timezone.now().date()
        )

    def expired(self):
        from django.utils import timezone
        return self.filter(
            contract_end__isnull=False,
            contract_end__lt=timezone.now().date()
        )


class NotebookLease(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Aktif'
        INACTIVE = 'inactive', 'Tidak Aktif'

    device_type = models.CharField(max_length=200)
    office_type = models.CharField(max_length=100, blank=True)
    email_license = models.EmailField(max_length=200, blank=True, db_index=True)
    asset_number = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    serial_number = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    box_number = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=300, blank=True, db_index=True)
    activation_date = models.CharField(max_length=50, blank=True)
    mac_address = models.CharField(max_length=100, blank=True)
    vendor_provider = models.CharField(max_length=200, blank=True, db_index=True)
    pdf_report_certificate = models.CharField(max_length=200, blank=True)
    pnbp_status = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to='notebook_docs/', null=True, blank=True)
    notes = models.TextField(blank=True)
    contract_start = models.DateField(null=True, blank=True)
    contract_end = models.DateField(null=True, blank=True, db_index=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    image = models.ImageField(upload_to='asset_images/', null=True, blank=True)
    import_month = models.CharField(max_length=7, default="2026-07", db_index=True)
    technical_specs = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = NotebookLeaseQuerySet.as_manager()

    class Meta:
        db_table = 'notebook_leases'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['import_month']),
        ]

    def __str__(self):
        return f"{self.device_type} - {self.user_name or '-'}"


class SoftwareApplication(models.Model):
    asset_name = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=100, blank=True)
    sub_class = models.CharField(max_length=150, db_index=True)
    owner = models.CharField(max_length=200, db_index=True)
    location = models.CharField(max_length=200, db_index=True)
    confidentiality = models.SmallIntegerField(null=True, blank=True)
    integrity = models.SmallIntegerField(null=True, blank=True)
    availability = models.SmallIntegerField(null=True, blank=True)
    value = models.SmallIntegerField(null=True, blank=True)
    import_month = models.CharField(max_length=7, default="2026-07", db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'software_applications'
        ordering = ['asset_name']
        indexes = [
            models.Index(fields=['import_month']),
        ]

    def __str__(self):
        return self.asset_name
