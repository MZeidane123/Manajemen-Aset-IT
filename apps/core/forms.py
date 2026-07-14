from django import forms
from .models import Asset, Category, Location, PhysicalAsset, SoftwareLicense, NotebookLease, SoftwareApplication


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = [
            'category', 'brand', 'model_name', 'serial_number', 'asset_number',
            'office_version', 'email_license_status', 'user_pc', 'location',
            'acquisition_date', 'price', 'vendor_name', 'vendor_contract_end',
            'status', 'notes',
        ]
        widgets = {
            'acquisition_date': forms.DateInput(attrs={'type': 'date'}),
            'vendor_contract_end': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, (forms.DateInput, forms.Textarea)):
                field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
            else:
                field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})

    def clean_serial_number(self):
        sn = self.cleaned_data['serial_number'].strip()
        qs = Asset.objects.filter(serial_number=sn)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Nomor seri sudah terdaftar di database.')
        return sn

    def clean_asset_number(self):
        an = self.cleaned_data['asset_number'].strip()
        qs = Asset.objects.filter(asset_number=an)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Nomor aset sudah terdaftar di database.')
        return an


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class PhysicalAssetForm(forms.ModelForm):
    class Meta:
        model = PhysicalAsset
        fields = [
            'asset_name', 'sub_class', 'operating_system', 'brand', 'model_name',
            'serial_number', 'owner', 'location', 'asset_number',
            'confidentiality', 'integrity', 'availability', 'notes', 'image', 'import_month',
            'technical_specs',
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'hidden', 'id': 'imageUpload'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'image':
                field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class SoftwareLicenseForm(forms.ModelForm):
    class Meta:
        model = SoftwareLicense
        fields = [
            'name', 'license_type', 'vendor', 'license_number', 'quantity',
            'location_install', 'room_location', 'purchase_date', 'status', 'notes', 'import_month',
        ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class NotebookLeaseForm(forms.ModelForm):
    class Meta:
        model = NotebookLease
        fields = [
            'device_type', 'office_type', 'email_license', 'asset_number', 'serial_number',
            'box_number', 'user_name', 'activation_date', 'mac_address', 'vendor_provider',
            'pdf_report_certificate', 'pnbp_status', 'notes', 'contract_start', 'contract_end',
            'status', 'image', 'import_month', 'technical_specs',
        ]
        widgets = {
            'contract_start': forms.DateInput(attrs={'type': 'date'}),
            'contract_end': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'hidden', 'id': 'imageUploadNotebook'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'image':
                field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})


class SoftwareApplicationForm(forms.ModelForm):
    class Meta:
        model = SoftwareApplication
        fields = [
            'asset_name', 'ip_address', 'sub_class', 'owner', 'location',
            'confidentiality', 'integrity', 'availability', 'value', 'import_month',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'})
