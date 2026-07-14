from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta, date
from decimal import Decimal
from apps.core.models import Category, Location, Asset
from apps.forms.models import ChangeRequest, ChangeRequestDocument
from apps.users.models import User
import random
import sys


class Command(BaseCommand):
    help = 'Seed demo data atau hapus semua data demo'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Hapus semua data demo')
        parser.add_argument('--force', action='store_true', help='Skip konfirmasi hapus')

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data(options['force'])
        else:
            self.seed_data(options['force'])

    # ── CLEAR ──────────────────────────────

    def clear_data(self, force):
        counts = {
            'ChangeRequestDocument': ChangeRequestDocument.objects.count(),
            'ChangeRequest': ChangeRequest.objects.count(),
            'Asset': Asset.objects.count(),
            'Location': Location.objects.count(),
            'Category': Category.objects.count(),
        }

        if not any(counts.values()):
            self.stdout.write(self.style.WARNING('Tidak ada data untuk dihapus.'))
            return

        self.stdout.write('Data yang akan dihapus:')
        for model, count in counts.items():
            self.stdout.write(f'  {model}: {count}')

        if not force:
            answer = input('\nYakin ingin menghapus semua data? (y/N): ')
            if answer.lower() != 'y':
                self.stdout.write(self.style.WARNING('Dibatalkan.'))
                return

        ChangeRequestDocument.objects.all().delete()
        ChangeRequest.objects.all().delete()
        Asset.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

        total = sum(counts.values())
        self.stdout.write(self.style.SUCCESS(f'{total} data berhasil dihapus.'))

    # ── SEED ───────────────────────────────

    def seed_data(self, force=False):
        if Asset.objects.exists() or Category.objects.exists() or Location.objects.exists():
            if force:
                self.clear_data(force=True)
            else:
                answer = input(self.style.WARNING('Data sudah ada. Hapus dulu? (y/N): '))
                if answer.lower() == 'y':
                    self.clear_data(force=True)
                else:
                    self.stdout.write(self.style.WARNING('Dibatalkan.'))
                    return

        today = timezone.now().date()

        # ── Kategori ────────────────────────
        categories = {
            'Laptop': 'Laptop/Notebook untuk operasional karyawan',
            'Server': 'Server fisik untuk infrastruktur aplikasi & database',
            'Access Point': 'Perangkat jaringan wireless indoor/outdoor',
            'Printer': 'Printer multifungsi untuk administrasi kantor',
            'Monitor': 'Monitor eksternal untuk workstation',
        }
        cat_objs = {}
        for name, desc in categories.items():
            cat_objs[name] = Category.objects.create(name=name, description=desc)
        self.stdout.write(f'  v {len(categories)} kategori')

        # ── Lokasi ──────────────────────────
        locations = {
            'Kantor Pusat - Gedung A': 'Lantai 1-3, Kantor Pusat Dahana, Subang',
            'Kantor Pusat - Gedung B': 'Lantai 1-2, Kantor Pusat Dahana, Subang',
            'Kantor Pusat - Gedung C': 'Lantai 1, Kantor Pusat Dahana, Subang',
            'Site Energetic Material Center': 'Kawasan EMC, Subang',
            'Site Handang': 'Site Handang, Jawa Barat',
            'Site Bojongsoang': 'Site Bojongsoang, Bandung',
            'Gudang Pusat': 'Gudang penyimpanan perangkat cadangan',
        }
        loc_objs = {}
        for name, desc in locations.items():
            loc_objs[name] = Location.objects.create(name=name, description=desc)
        self.stdout.write(f'  v {len(locations)} lokasi')

        # ── User ────────────────────────────
        admin = User.objects.filter(is_superuser=True).first()
        editor = User.objects.filter(role='editor').first()
        viewer = User.objects.filter(role='viewer').first()

        if not all([admin, editor, viewer]):
            self.stdout.write(self.style.WARNING('User seed belum ada. Jalankan python manage.py seed_users'))
            return

        # ── Aset (100 per tahun) ────────────
        brands = {
            'Laptop': [
                ('Lenovo', 'ThinkPad X1 Carbon Gen 10', 26500000, 35000000),
                ('Lenovo', 'ThinkPad X1 Carbon Gen 11', 28500000, 35000000),
                ('Lenovo', 'ThinkPad X1 Carbon Gen 12', 31000000, 38000000),
                ('Lenovo', 'ThinkPad T14s Gen 4', 24000000, 30000000),
                ('Lenovo', 'ThinkPad P16s', 32000000, 38000000),
                ('Dell', 'Latitude 5530', 21000000, 27000000),
                ('Dell', 'Latitude 5540', 22500000, 29000000),
                ('Dell', 'Latitude 7450', 25000000, 32000000),
                ('Dell', 'Latitude 7650', 27000000, 34000000),
                ('HP', 'EliteBook 840 G10', 24500000, 31000000),
                ('HP', 'EliteBook 840 G11', 26000000, 33000000),
                ('HP', 'ProBook 450 G11', 18000000, 24000000),
                ('HP', 'ProBook 460 G11', 19500000, 25500000),
                ('Apple', 'MacBook Pro M3', 35900000, 42000000),
                ('Apple', 'MacBook Air M3', 22000000, 28000000),
                ('ASUS', 'Zenbook 14 OLED', 18500000, 24000000),
                ('ASUS', 'ExpertBook B5', 17000000, 22000000),
            ],
            'Server': [
                ('Dell', 'PowerEdge R750', 350000000, 420000000),
                ('Dell', 'PowerEdge R650', 295000000, 360000000),
                ('Dell', 'PowerEdge R760', 410000000, 480000000),
                ('Dell', 'PowerEdge R460', 195000000, 250000000),
                ('HPE', 'ProLiant DL380 Gen11', 450000000, 520000000),
                ('HPE', 'ProLiant DL20 Gen11', 185000000, 240000000),
                ('HPE', 'ProLiant DL360 Gen11', 380000000, 450000000),
                ('Lenovo', 'ThinkSystem SR650 V2', 320000000, 390000000),
                ('Lenovo', 'ThinkSystem SR250 V2', 145000000, 195000000),
            ],
            'Access Point': [
                ('Cisco', 'Meraki MR46', 12000000, 17000000),
                ('Cisco', 'Meraki MR56', 15500000, 21000000),
                ('Cisco', 'Meraki MR36', 9500000, 13500000),
                ('Ubiquiti', 'UniFi 6 Pro', 4200000, 6500000),
                ('Ubiquiti', 'UniFi 6 Enterprise', 6800000, 9500000),
                ('Ruckus', 'R770', 14000000, 19000000),
                ('Aruba', 'AP-635', 11000000, 15500000),
            ],
            'Printer': [
                ('HP', 'LaserJet Pro M402n', 6500000, 9000000),
                ('HP', 'LaserJet Pro M404dn', 8500000, 11500000),
                ('HP', 'Color LaserJet Pro M454dw', 9500000, 13000000),
                ('Canon', 'imageCLASS MF453dw', 7800000, 10500000),
                ('Canon', 'imageRUNNER C3326i', 15000000, 21000000),
                ('Epson', 'WorkForce Pro WF-4830', 5500000, 7500000),
                ('Brother', 'HL-L6400DW', 8000000, 11000000),
            ],
            'Monitor': [
                ('Samsung', 'Smart Monitor M8 32"', 6500000, 9500000),
                ('Dell', 'UltraSharp U2723QE', 8500000, 12000000),
                ('Dell', 'P2723QE', 7200000, 10000000),
                ('LG', '27UL850-W', 6800000, 9500000),
                ('LG', '27UP850-W', 7500000, 10500000),
                ('ASUS', 'ProArt PA278QV', 7000000, 9800000),
                ('BenQ', 'PD2706UA', 9000000, 12500000),
            ],
        }

        user_names = [
            'Budi Santoso', 'Siti Rahmawati', 'Ahmad Fauzi', 'Rudi Hermawan',
            'Fitri Handayani', 'Citra Anggraini', 'Dewi Lestari', 'Indra Permana',
            'Agus Wijaya', 'Doni Prasetyo', 'Eko Prasetyo', 'Wati Susilawati',
            'Hendra Kurniawan', 'Maya Sari', 'Rizki Pratama', 'Anisa Putri',
            'Fajar Nugroho', 'Lina Marlina', 'Andi Saputra', 'Rina Wulandari',
            'Tono Sugiarto', 'Bunga Citra', 'Dian Permata', 'Eko Wahyudi',
            'Gilang Ramadhan', 'Hana Kartika', 'Irfan Hakim', 'Joko Susilo',
            'Kartika Sari', 'Luthfi Hasan', 'Mega Putri', 'Nanda Pratama',
            'Olivia Chen', 'Putra Pratama', 'Rizal Akbar', 'Salsa Billa',
            'Taufik Rahman', 'Ulya Maghfiroh', 'Vino G Bastian', 'Winda Astuti',
        ]

        vendors = [
            'PT. Anugrah Perkasa', 'PT. Solusi Teknologi', 'PT. Data Citra Mandiri',
            'PT. Network Solution', 'PT. Data Center Asia', 'PT. iCenter Indonesia',
            'PT. Elektronik Cemerlang', 'PT. Jaringan Prima', 'PT. Mitra Komputama',
            'PT. Sistem Informasi Nusantara', 'PT. Teknologi Global Mandiri', 'PT. Digital Solusi Indonesia',
        ]

        offices = [
            'Microsoft 365 Apps', 'Microsoft 365 Basic', 'Google Workspace',
            'Microsoft 365 E3', 'Microsoft 365 E5', '',
        ]

        license_statuses = ['Active', 'Active', 'Active', 'Expired', 'Trial', '']

        status_pool = ['active'] * 70 + ['maintenance'] * 15 + ['retired'] * 10 + ['disposed'] * 5

        notes_options = [
            '', '', '', '', '', '', '', '', '', '',
            'Unit baru, belum ada catatan',
            'Dalam masa garansi',
            'Garansi expired',
            'Sudah upgrade RAM',
            'Sedang dalam perbaikan',
            'Cadangan',
            'Sudah tidak digunakan',
            'Perlu diganti',
            'Kondisi prima',
            'Layak pakai',
            'Ada kerusakan minor',
            'Perlu kalibrasi',
            'Sudah migrasi',
            'Backup unit',
            'Spare part tersedia',
        ]

        asset_counter = 0
        years = [2023, 2024, 2025]
        assets_data = []

        for year in years:
            for i in range(100):
                asset_counter += 1
                cat_name = random.choice(list(brands.keys()))
                brand_list = brands[cat_name]
                brand_info = random.choice(brand_list)
                brand, model_base, price_min, price_max = brand_info
                model = f'{model_base}'

                # Unique serial
                serial_prefix = {'Laptop': 'LP', 'Server': 'SRV', 'Access Point': 'AP', 'Printer': 'PRN', 'Monitor': 'MON'}
                serial = f'{serial_prefix[cat_name]}-{year}-{asset_counter:04d}'
                asset_num = f'AST-{asset_counter:04d}'

                loc_name = random.choice(list(locations.keys()))
                acq_month = random.randint(1, 12)
                acq_day = random.randint(1, 28)
                acq_date = date(year, acq_month, acq_day)

                price = Decimal(str(random.randint(price_min, price_max)))

                contract_end_year = year + random.randint(2, 4)
                contract_end = date(min(contract_end_year, 2028), random.randint(1, 12), random.randint(1, 28))

                status = random.choice(status_pool)
                user_pc = random.choice(user_names) if cat_name in ['Laptop'] else ''
                office = random.choice(offices) if cat_name in ['Laptop'] else ''
                email_license = random.choice(license_statuses) if cat_name in ['Laptop'] else ''
                vendor = random.choice(vendors)
                notes = random.choice(notes_options)

                # Unique model suffix
                if cat_name in ['Laptop', 'Server']:
                    suffix_variants = ['A', 'B', 'C', 'Pro', 'Standard', 'Plus', 'Ultra', 'Lite']
                    model = f'{model_base} {random.choice(suffix_variants)}'

                assets_data.append((brand, model, serial, asset_num, cat_name, loc_name, acq_date, price, vendor, contract_end, status, user_pc, office, email_license, notes))

        for b, model, serial, asset_num, cat_name, loc_name, acq_date, price, vendor, contract_end, status, user_pc, office, email_license, notes in assets_data:
            Asset.objects.create(
                category=cat_objs[cat_name],
                brand=b,
                model_name=model,
                serial_number=serial,
                asset_number=asset_num,
                office_version=office,
                email_license_status=email_license,
                user_pc=user_pc,
                location=loc_objs[loc_name],
                acquisition_date=acq_date,
                price=price,
                vendor_name=vendor,
                vendor_contract_end=contract_end,
                status=status,
                notes=notes,
                created_by=editor,
            )

        self.stdout.write(f'  v {len(assets_data)} aset')

        # ── Change Request ──────────────────
        cr_titles = [
            'Penambahan Resource Server',
            'Migrasi Aplikasi ke Server Baru',
            'Upgrade Kapasitas Storage',
            'Pergantian Access Point Rusak',
            'Penambahan Printer di Lantai 3',
            'Upgrade Monitor untuk Desainer',
            'Penggantian Laptop Manager',
            'Perluasan Jaringan WiFi',
            'Backup Server Otomatis',
            'Penggantian UPS Rusak',
            'Penambahan License Microsoft 365',
            'Upgrade Firmware Access Point',
            'Penggantian Kabel Jaringan',
            'Penambahan Switch Managed',
            'Penggantian Hardisk Server',
            'Upgrade RAM Server CRM',
            'Penambahan Printer Multifungsi',
            'Penggantian Monitor 4K',
            'Migrasi Database ke SSD',
            'Penggantian Laptop Arsip',
            'Penambahan Server Backup',
            'Upgrade License Google Workspace',
            'Penggantian Access Point Outdoor',
            'Penambahan Slot Rack Server',
            'Penggantian Printer Label',
            'Upgrade Infrastruktur Cloud',
            'Penggantian UPS 3KVA',
            'Penambahan NAS Storage',
            'Penggantian Kabel Fiber',
            'Upgrade Sistem Monitoring',
        ]

        cr_descs = [
            'Permohonan penambahan resource CPU dan memory pada server untuk menangani beban aplikasi yang meningkat.',
            'Permohonan migrasi aplikasi dari server lama ke server baru dengan spesifikasi lebih tinggi.',
            'Permohonan upgrade kapasitas storage dari 4TB menjadi 12TB untuk mengakomodasi pertumbuhan data.',
            'Permohonan penggantian perangkat yang sudah tidak berfungsi dengan unit baru.',
            'Permohonan penambahan perangkat untuk mendukung operasional di lantai baru.',
            'Permohonan upgrade perangkat untuk meningkatkan produktivitas tim.',
        ]

        crs_data = [
            (cr_titles[0], cr_descs[0], '', 'signed'),
            (cr_titles[1], cr_descs[1], 'Aplikasi CRM saat ini berjalan di server dengan spesifikasi terbatas.', 'draft'),
            (cr_titles[2], cr_descs[2], '', 'draft'),
        ]

        for title, desc, reason, status in crs_data:
            cr = ChangeRequest.objects.create(
                title=title,
                description=desc,
                reason=reason,
                status=status,
                created_by=editor,
            )
            if status == 'signed':
                cr.sign(
                    name='Budi Santoso, S.T.',
                    position='Head of IT Infrastructure'
                )

        self.stdout.write(f'  v 3 change request (1 dengan TTD digital)')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Data demo berhasil diisi!'))
        self.stdout.write(f'  Kategori: {len(categories)}')
        self.stdout.write(f'  Lokasi:   {len(locations)}')
        self.stdout.write(f'  Aset:     {len(assets_data)} (100 per tahun)')
        self.stdout.write(f'  CR:       {len(crs_data)}')
