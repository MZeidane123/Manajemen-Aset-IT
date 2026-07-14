from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from decimal import Decimal
from apps.core.models import PhysicalAsset, SoftwareLicense, NotebookLease, SoftwareApplication


@login_required
def index(request):
    cat_filter = request.GET.get('category', 'all')

    # Base querysets
    phys_qs = PhysicalAsset.objects.all()
    lic_qs = SoftwareLicense.objects.all()
    note_qs = NotebookLease.objects.all()
    app_qs = SoftwareApplication.objects.all()

    # Apply category filter
    if cat_filter == 'physical':
        lic_qs = lic_qs.none()
        note_qs = note_qs.none()
        app_qs = app_qs.none()
    elif cat_filter == 'notebook':
        phys_qs = phys_qs.none()
        lic_qs = lic_qs.none()
        app_qs = app_qs.none()
    elif cat_filter == 'software':
        phys_qs = phys_qs.none()
        note_qs = note_qs.none()

    # Counts
    physical_count = phys_qs.count()
    license_count = lic_qs.count()
    notebook_count = note_qs.count()
    app_count = app_qs.count()
    total_assets = physical_count + license_count + notebook_count + app_count

    # Active status mapping
    active_phys = physical_count
    active_lic = lic_qs.filter(status__iexact='aktif').count() + lic_qs.filter(status__iexact='active').count()
    active_note = note_qs.filter(status=NotebookLease.Status.ACTIVE).count()
    active_app = app_count
    active_assets = active_phys + active_lic + active_note + active_app

    # Inactive/Decommissioned status mapping
    decom_note = note_qs.filter(status=NotebookLease.Status.INACTIVE).count()
    decom_lic = lic_qs.exclude(status__iexact='aktif').exclude(status__iexact='active').count()
    decommissioned_assets = decom_note + decom_lic

    # Compliance Score calculation
    compliant_phys = phys_qs.exclude(serial_number='').exclude(asset_number__isnull=True).exclude(asset_number='').exclude(location='').count()
    compliant_note = note_qs.exclude(serial_number='').exclude(asset_number__isnull=True).exclude(asset_number='').count()
    compliant_lic = lic_qs.exclude(license_number='').count()
    compliant_app = app_qs.exclude(ip_address='').exclude(location='').count()

    compliant_total = compliant_phys + compliant_note + compliant_lic + compliant_app
    compliance_score = round((compliant_total / (total_assets or 1)) * 100)

    total_value = Decimal('0')
    budget_utilization = 0.0

    # Group by category
    cat_counts = {}
    
    if cat_filter == 'all':
        if physical_count > 0:
            cat_counts['PHYSICAL ASSETS'] = physical_count
        if notebook_count > 0:
            cat_counts['NOTEBOOK LEASES'] = notebook_count
        if license_count > 0:
            cat_counts['SOFTWARE LICENSES'] = license_count
        if app_count > 0:
            cat_counts['SOFTWARE APPLICATIONS'] = app_count
    else:
        if cat_filter == 'physical':
            for item in phys_qs.values('sub_class').annotate(count=Count('id')):
                name = (item['sub_class'] or 'UNCLASSIFIED').strip().upper()
                cat_counts[name] = cat_counts.get(name, 0) + item['count']
                
        if cat_filter == 'notebook':
            for item in note_qs.values('device_type').annotate(count=Count('id')):
                name = (item['device_type'] or 'UNKNOWN DEVICE').strip().upper()
                cat_counts[name] = cat_counts.get(name, 0) + item['count']

        if cat_filter == 'software':
            for item in app_qs.values('sub_class').annotate(count=Count('id')):
                v = item['sub_class']
                name = v.strip().upper() if v and v.strip() and v.strip() != '-' else 'UNCLASSIFIED'
                cat_counts[name] = cat_counts.get(name, 0) + item['count']
            
            for item in lic_qs.values('license_type').annotate(count=Count('id')):
                v = item['license_type']
                name = v.strip().upper() if v and v.strip() and v.strip() != '-' else 'UNKNOWN LICENSE'
                cat_counts[name] = cat_counts.get(name, 0) + item['count']

    categories_labels = list(cat_counts.keys())
    categories_data = list(cat_counts.values())

    status_items = [
        {'label': 'Aktif', 'count': active_assets, 'color': '#10b981'},
        {'label': 'Tidak Aktif', 'count': decommissioned_assets, 'color': '#ef4444'},
    ]

    # Pie Chart Data & Title
    loc_counts = {}
    pie_chart_title = 'Sebaran Lokasi'
    pie_chart_subtitle = 'Distribusi aset per lokasi fisik'

    if cat_filter == 'notebook':
        pie_chart_title = 'Sebaran Vendor'
        pie_chart_subtitle = 'Distribusi aset berdasarkan penyedia layanan'
        for item in note_qs.values('vendor_provider').annotate(count=Count('id')):
            name = (item['vendor_provider'] or 'UNKNOWN VENDOR').strip().upper()
            loc_counts[name] = loc_counts.get(name, 0) + item['count']
    elif cat_filter == 'software':
        pie_chart_title = 'Vendor & Pemilik'
        pie_chart_subtitle = 'Distribusi berdasarkan entitas pengelola'
        for item in lic_qs.values('vendor').annotate(count=Count('id')):
            v = item['vendor']
            name = v.strip().upper() if v and v.strip() and v.strip() != '-' else 'UNKNOWN VENDOR'
            loc_counts[name] = loc_counts.get(name, 0) + item['count']
        for item in app_qs.values('owner').annotate(count=Count('id')):
            o = item['owner']
            name = o.strip().upper() if o and o.strip() and o.strip() != '-' else 'UNKNOWN OWNER'
            loc_counts[name] = loc_counts.get(name, 0) + item['count']
    else:
        pie_chart_title = 'Sebaran Lokasi'
        pie_chart_subtitle = 'Distribusi aset per lokasi fisik'
        for item in phys_qs.values('location').annotate(count=Count('id')):
            name = (item['location'] or 'UNKNOWN').strip().upper()
            loc_counts[name] = loc_counts.get(name, 0) + item['count']
        for item in lic_qs.values('location_install').annotate(count=Count('id')):
            name = (item['location_install'] or 'UNKNOWN').strip().upper()
            loc_counts[name] = loc_counts.get(name, 0) + item['count']
        for item in app_qs.values('location').annotate(count=Count('id')):
            name = (item['location'] or 'UNKNOWN').strip().upper()
            loc_counts[name] = loc_counts.get(name, 0) + item['count']

    locations_labels = list(loc_counts.keys())
    locations_data = list(loc_counts.values())

    # List Chart Data & Title
    list_chart_title = 'Ringkasan Lisensi Email'
    list_chart_subtitle = 'Status lisensi email seluruh aset'
    
    if cat_filter == 'notebook':
        list_chart_title = 'Ringkasan MS Office'
        list_chart_subtitle = 'Jenis MS Office pada notebook'
        email_lic_summary = [
            {'label': item['office_type'] or 'Tidak Diketahui', 'count': item['count']}
            for item in note_qs.values('office_type').annotate(count=Count('id')).order_by('office_type')
        ]
    elif cat_filter == 'physical':
        list_chart_title = 'Merek Aset'
        list_chart_subtitle = 'Distribusi aset berdasarkan brand'
        email_lic_summary = [
            {'label': item['brand'] or 'Tidak Diketahui', 'count': item['count']}
            for item in phys_qs.values('brand').annotate(count=Count('id')).order_by('-count')[:5]
        ]
    else:
        email_lic_summary = []
        for item in lic_qs.values('status').annotate(count=Count('id')).order_by('status'):
            v = item['status']
            label = v.strip().title() if v and v.strip() and v.strip() != '-' else 'Tidak Diketahui'
            email_lic_summary.append({'label': label, 'count': item['count']})

    context = {
        'total_assets': total_assets,
        'active_assets': active_assets,
        'maintenance_assets': 0,
        'decommissioned_assets': decommissioned_assets,
        'total_value': total_value,
        'compliance_score': compliance_score,
        'budget_utilization': budget_utilization,
        'categories_labels': categories_labels,
        'categories_data': categories_data,
        'status_items': status_items,
        'locations_labels': locations_labels,
        'locations_data': locations_data,
        'list_chart_data': email_lic_summary,
        'cat_filter': cat_filter,
        'pie_chart_title': pie_chart_title,
        'pie_chart_subtitle': pie_chart_subtitle,
        'list_chart_title': list_chart_title,
        'list_chart_subtitle': list_chart_subtitle,
    }
    return render(request, 'dashboard/index.html', context)
