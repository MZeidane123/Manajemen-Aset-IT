from django.contrib import admin
from .models import Category, Location, Asset, PhysicalAsset, SoftwareLicense, NotebookLease


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['brand', 'category', 'serial_number', 'asset_number', 'status', 'location', 'vendor_contract_end']
    list_filter = ['status', 'category', 'location']
    search_fields = ['brand', 'serial_number', 'asset_number', 'user_pc']
    date_hierarchy = 'acquisition_date'


@admin.register(PhysicalAsset)
class PhysicalAssetAdmin(admin.ModelAdmin):
    list_display = ['asset_name', 'brand', 'sub_class', 'serial_number', 'owner', 'location']
    list_filter = ['sub_class', 'owner', 'location']
    search_fields = ['asset_name', 'brand', 'serial_number', 'asset_number']


@admin.register(SoftwareLicense)
class SoftwareLicenseAdmin(admin.ModelAdmin):
    list_display = ['name', 'license_type', 'vendor', 'quantity', 'status']
    list_filter = ['license_type', 'vendor', 'status']
    search_fields = ['name', 'vendor', 'license_number']


@admin.register(NotebookLease)
class NotebookLeaseAdmin(admin.ModelAdmin):
    list_display = ['device_type', 'user_name', 'asset_number', 'vendor_provider', 'contract_end', 'status']
    list_filter = ['vendor_provider', 'status', 'device_type']
    search_fields = ['device_type', 'user_name', 'asset_number', 'serial_number']
