## BUSINESS REQUIREMENT DOCUMENT (BRD) SISTEM INFORMASI Manajemen Aset IT 

## PT DAHANA (Persero) — FASE 1 

|**Informasi Dokumen**||
|---|---|
|**Nama Proyek**|Sistem Informasi Manajemen Aset IT|
|**Fase**|Fase 1 — Modul Operasional Inventaris,<br>Lisensi, & Infrastruktur Server|
|**Versi Dokumen**|1.0|
|**Tanggal**|08 Juli 2026|
|**Status**|Draft For Review|



# DAFTAR ISI 

## BAB I: PENDAHULUAN 

## 1.1 Latar Belakang dan Rumusan Masalah 

Manajemen aset Teknologi Informasi (IT) saat ini menjadi tantangan besar bagi perusahaan seiring dengan meningkatnya jumlah perangkat operasional yang mencapai ratusan unit laptop, server, access point, hingga berbagai lisensi perangkat lunak. Pengelolaan seluruh aset tersebut masih dilakukan secara manual menggunakan format Excel, yang dinilai tidak fleksibel dan menyulitkan proses pembaruan data secara _real-time_ . 

Ketidakteraturan dalam pencatatan manual ini berisiko menimbulkan ketidaksinkronan data antar staf IT, terutama saat terjadi penambahan aset baru di pertengahan tahun yang tidak segera terdata dalam dokumen pusat. Selain itu, tim IT menghadapi kesulitan dalam memantau detail teknis yang krusial seperti nomor seri, nomor aset, versi Office, hingga status lisensi email untuk setiap unit perangkat yang tersebar. Kebutuhan akan digitalisasi semakin mendesak karena adanya tuntutan audit tahunan yang memerlukan riwayat perolehan dan status aset yang akurat dan transparan. Tanpa sistem digital, proses peninjauan dan pemantauan siklus hidup aset— termasuk perangkat yang sudah habis masa kontraknya dengan vendor—menjadi tidak optimal dan kurang profesional. 

|**No**|**Aspek**|**Kondisi Saat Ini**|**Permasalahan**|
|---|---|---|---|
|**1**|**Pengelolaan**<br>**Asset Register**|Dicatat manual<br>menggunakan format<br>spreadsheet Excel<br>terpisah.|Tidak fleksibel, sulit melakukan<br>pembaruan data secara_real-_<br>_time_, dan terdapat risiko<br>ketidaksinkronan data antar staf<br>IT.|
|**2**|**Pemantauan**<br>**Detail Teknis &**<br>**Lisensi**|Pendataan detail (nomor<br>seri, nomor aset, versi<br>Office, status lisensi<br>email) tersebar.|Tim IT kesulitan memantau<br>spesifikasi teknis dan siklus<br>hidup kontrak perangkat/vendor<br>secara transparan.|
|**3**|**Formulir**<br>**Administrasi**<br>**(Change**<br>**Request)**|Pengisian formulir<br>administrasi masih<br>manual dan<br>terfragmentasi.|Memperlama proses persetujuan<br>dan menghasilkan tumpukan<br>dokumen fisik.|



|**No**|**Aspek**|**Kondisi Saat Ini**|**Permasalahan**|
|---|---|---|---|
|4|**Riwayat Aset**<br>**untuk Audit**|Rekapitulasi riwayat<br>perolehan aset dilakukan<br>manual saat audit<br>tahunan.|Proses peninjauan lambat, tidak<br>optimal, dan kurang transparan<br>untuk kebutuhan audit.|



## 1.2 Tujuan 

Pengembangan Aplikasi CMDB (Configuration Management Database) Fase 1 bertujuan untuk: 

1. **Digitalisasi Asset Register:** Membangun sistem aplikasi terpusat untuk mendigitalisasi pencatatan ratusan unit laptop, server, access point, dan lisensi software. 

2. **Sentralisasi & Transparansi Data:** Menyediakan satu platform terpadu yang mempermudah pemantauan detail teknis (nomor seri, nomor aset, versi Office, status lisensi email) secara _real-time_ . 

3. **Efisiensi Administrasi Berbasis E-Sign:** Mengintegrasikan formulir administratif (seperti _Change Request_ ) ke dalam satu platform digital yang mendukung tanda tangan elektronik. 

4. **Otomatisasi Audit Trail:** Menyediakan catatan riwayat perolehan aset secara otomatis per tahun untuk menyediakan data valid, akurat, dan transparan bagi audit tahunan. 

## 1.3 Ruang Lingkup Dokumen 

Dokumen BRD ini mencakup kebutuhan untuk **Fase 1** pengembangan sistem, yang terdiri dari: 

## 1.3.1 Modul yang Dicakup (In Scope) 

|1.3.1 Modul yang Dicakup (In|Scope)||
|---|---|---|
|**No**|**Modul**|**Deskripsi Singkat**|
|1|**CMDB Core (Asset**<br>**Register)**|Pencatatan, pembaruan, dan<br>pemantauan data inventaris<br>perangkat keras dan<br>perangkat lunak|
|2|**Formulir Digital & E-Sign**|Digitalisasi form administrasi<br>(termasuk_Change Request_)<br>dengan fitur tanda tangan|



|**No**|**Modul**|**Deskripsi Singkat**|
|---|---|---|
|||digital|
|3|**Audit Trail & Lifecycle**<br>**Tracking**|Pencatatan riwayat aset<br>otomatis dan pemantauan<br>masa kontrak vendor.|



## 1.3.2 Batasan Masalah (Out of Scope) 

Modul di luar manajemen aset internal IT (seperti manajemen keuangan IT komprehensif, pengadaan/procurement eksternal skala besar) tidak termasuk dalam ruang lingkup Fase 1. 

## BAB II: PROSES BISNIS 

## 2.1 Proses Bisnis Saat Ini (As-Is) 

## 2.1.1 Pengelolaan Asset Register (Pencatatan Aset) — As-Is 

## **Kondisi Saat Ini:** 

1. Tim internal IT melakukan pencatatan dan pembaruan data inventaris secara manual menggunakan file spreadsheet Excel terpisah. 

2. Saat terjadi penambahan aset baru di pertengahan tahun, staf IT yang menangani seringkali terlambat atau lupa memperbarui dokumen pusat, sehingga memicu ketidaksinkronan data antar staf. 

## **Permasalahan Utama:** 

- Format Excel tidak fleksibel 

- menyulitkan pembaruan data secara _real-time_ 

## 2.1.2 Pemantauan Spesifikasi Teknis & Lisensi — As-Is 

## **Kondisi Saat Ini:** 

1. Pencatatan komponen krusial seperti nomor seri, nomor aset, versi Microsoft Office, hingga status lisensi email per unit perangkat masih tersebar di berbagai catatan parsial atau ingatan staf. 

## **Permasalahan Utama:** 

- kesulitan besar dalam memantau detail teknis perangkat 

- melacak masa berlaku siklus hidup aset 

## 2.1.3 Formulir Administrasi & Pelaporan Audit — As-Is 

## **Kondisi Saat ini:** 

1. Pengisian formulir administratif (seperti _Change Request_ ) dilakukan secara manual di atas kertas fisik, ditandatangani basah, dan direkap secara berkala untuk keperluan pemantauan tahunan. 

## **Permasalahan Utama:** 

- Dokumen administrasi terfragmentasi, memicu tumpukan berkas fisik 

- menyulitkan peninjauan riwayat aset yang cepat dan transparan saat audit tahunan tiba. 

## 2.2 Proses Bisnis yang Diharapkan (To-Be) 

## 2.2.1 Konsep "One Gate System" 

Sistem baru akan menerapkan konsep sentralisasi manajemen aset IT melaui Aplikasi CMDB terpusat. Seluruh aktivitas input data, perubahan spesifikasi, pengajuan kebutuhan, hingga persetujuan formulir _Change Request_ wajib berjalan di dalam satu platform digital terintegrasi. Data riwayat aset akan terekam otomatis demi menjamin transparansi data yang valid untuk kebutuhan internal maupun audit pihak eksternal 

## 2.2.2 Modul CMDB Core (Asset Register) — To-Be 

## **Alur Proses Baru:** 

|**Tahap**|**Aktor**|**Aktivitas**|
|---|---|---|
|1|**Editor**|Membuka aplikasi<br>CMDB/Custom untuk<br>memperbarui atau menginput<br>aset IT baru yang masuk ke<br>perusahaan.|
|2|**Editor**|Mengisi data teknis secara<br>lengkap pada formulir digital,<br>meliputi: merek, nomor seri,<br>informasi lisensi email,<br>hingga detail lokasi<br>penempatan aset tersebut|
|3|**Sistem**|Menyimpan data ke dalam<br>database terpusat secara<br>_real-time_, meminimalkan<br>risiko ketidaksinkronan data,<br>serta mencatat riwayat<br>perolehan aset secara<br>otomatis untuk kebutuhan<br>audit.|
|4|**Viewer (Level Manager)**|Mengakses dasbor aplikasi<br>kapan saja untuk memantau<br>status, jumlah, dan kondisi<br>siklus hidup aset IT secara<br>mudah, akurat, dan|



|**Tahap**|**Aktor**|**Aktivitas**|
|---|---|---|
|||profesional.|



## **Catatan Penting:** 

- Sistem mengunci hak perubahan data aset hanya untuk peran Editor dan merekam riwayatnya secara otomatis untuk kebutuhan audit. 

## 2.2.3 Digitalisasi Formulir & Dokumentasi Digital (E-Sign) — To-Be 

## **Alur Proses Baru:** 

|**Tahap**|**Aktor**|**Aktivitas**|
|---|---|---|
|1|**Editor**|Mengakses menu<br>administrasi digital, lalu<br>mengisi dan mengunggah<br>dokumen persetujuan seperti|



|**Tahap**|**Aktor**|**Aktivitas**|
|---|---|---|
|||_Form Change Request_yang<br>telah ditandatangani.|
|2|**Sistem**|Memproses dokumen digital<br>tersebut, mengunci berkas<br>pengajuan, serta<br>menyimpannya ke dalam<br>pangkalan data arsip terpusat<br>agar tidak terfragment|
|3|**Sistem**|Otomatis mencatatkan<br>riwayat dokumen dan<br>menerbitkannya ke dalam<br>dasbor monitoring<br>administrasi.|
|4|**Viewer**|Mengakses modul formulir<br>digital untuk memonitor<br>status pengajuan serta<br>melihat isi dokumen_Change_<br>_Request_yang terarsip secara<br>transparan.|



## **Catatan Penting:** 

- Pengelolaan formulir digital dilakukan sepenuhnya oleh Editor, sedangkan level Manager ke atas berfungsi memonitor riwayat berkas pada sistem. 

**==> picture [178 x 335] intentionally omitted <==**

**----- Start of picture text -----**<br>
© EDITOR/TIM IT<br>> Isi & Upload Form<br>Change Request Digital<br>(Perubahan Fitur Aplikasi)<br>© SISTEM<br>Q Apakah Semua Field<br>Wajib Sudah Diisi?<br>Tidak Lengkap Lengkap<br>“ Peringatan:8: . :Teks @ Kunci. Berkas & Simpan.<br>Spesifikasi ke Arsip Terpusat<br>Wajib Diisi Lengkap p Terpu<br>} Terbitkan Dokumen ke<br>Dasbor<br>(Audit Trail)<br>@ VIEWER (LevegManager ke Atas)<br>Q Memonitor Status &<br>Melihat<br>Arsip Dokumen Form Digital<br>**----- End of picture text -----**<br>


## BAB III: RUANG LINGKUP 

## 3.1 Modul 1: CMDB Core (Asset Register &  Lifecycle Tracking) 

**Tujuan:** Mendata, mengelola, dan memantau seluruh siklus hidup aset IT perusahaan secara terpusat untuk mengeliminasi pencatatan manual berbasis Excel. 

|**Fitur**|**Deskripsi**|
|---|---|
|**Input & Update Aset**|Formulir digital untuk mendaftarkan dan<br>memperbarui aset hardware baru (Laptop,<br>Server,_Access Point_) ke dalam sistem<br>terpusat.|
|**Pencatatan Detail Spesifikasi**|Field wajib untuk mencatat aspek teknis<br>krusial meliputi merek, nomor seri perangkat,<br>informasi lisensi email, hingga versi software.|



|**Fitur**|**Deskripsi**|
|---|---|
|**Manajemen Lokasi Aset**|Pencatatan lokasi penempatan fisik aset di<br>seluruh area operasional perusahaan untuk<br>memudahkan proses inventarisasi.|
|**Tracking Siklus Hidup & Kontrak**|Fitur pemantauan status operasional<br>perangkat, mulai dari aset aktif, perbaikan,<br>hingga pelacakan masa berlaku kontrak<br>dengan vendor.|



## 3.2 Modul 2: Formulir & Arsip Digital 

**Tujuan:** Mengintegrasikan dan mendigitalisasi formulir administrasi operasional TI ke dalam satu platform terpusat agar dokumen tidak terfragmentasi atau hilang. 

|**Fitur**|**Deskripsi**|
|---|---|
|**Digitalisasi Form Change Request**|Pengisian formulir permohonan perubahan<br>fitur aplikasi secara digital langsung di dalam<br>sistem.|
|**Upload Dokumentasi & E-Sign**|Fitur untuk mengunggah berkas pendukung<br>administrasi yang telah ditandatangani secara<br>elektronik (_e-sign_).|
|**Penguncian Dokumen Otomatis**|Berkas administrasi yang sudah selesai<br>diproses akan dikunci oleh sistem secara<br>otomatis untuk mencegah manipulasi data<br>pasca-persetujuan.|
|**Sentralisasi Arsip Digital**|Penyimpanan seluruh dokumen persetujuan<br>ke dalam database terpusat, menggantikan<br>penyimpanan fisik di lemari arsip.|



## 3.3 Modul 3: Dashboard Monitoring & Audit Trail 

**Tujuan:** Menyediakan visualisasi kondisi aset yang akurat ( _Single Source of Truth_ ) bagi jajaran manajemen serta menyediakan data riwayat yang transparan untuk kebutuhan audit tahunan. 

|**Fitur**|**Deskripsi**|
|---|---|
|**Dasbor Pemantauan Real-time**|Tampilan grafik visual yang menyajikan<br>status, jumlah, sebaran lokasi, dan kondisi<br>ratusan unit aset IT secara_real-time_.|
|**Audit Trail Otomatis**|Sistem merekam secara otomatis riwayat<br>perolehan aset, waktu input, serta rekam<br>jejak perubahan status aset per tahun untuk<br>kebutuhan audit tahunan.|
|**Akses Khusus Read-Only**|Pembatasan halaman pemantauan dasbor<br>dan arsip dokumen yang dikunci khusus<br>untuk level Manager ke atas sebatas fungsi<br>melihat data dan monitoring.|



## BAB IV: KEBUTUHAN FUNGSIONAL 

## 4.1 Kebutuhan Logika Bisnis 

|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|REQ-LOGIC-01|Editor|Sistem WAJIB<br>membuka akses<br>penuh (_Full Access_)<br>tanpa batasan bagi<br>Editor untuk<br>melakukan fungsi<br>_Create, Read,_<br>_Update, dan Delete_<br>(CRUD) pada seluruh<br>modul data aset IT,<br>pengelolaan kategori,<br>dan dokumen<br>administrasi.|High|
|REQ-LOGIC-02|Viewer|Sistem WAJIB<br>membatasi hak<br>akses jajaran<br>manajemen mulai<br>dari level Manager<br>ke atas sebagai<br>Viewer, di mana<br>seluruh tombol<br>manipulasi data<br>(_add, edit, delete_)<br>dihilangkan dan<br>sistem hanya<br>menampilkan data<br>dalam format baca<br>saja (_Read-Only_)<br>untuk fungsi<br>monitoring.|High|
|REQ-LOGIC-03|Sistem|Sistem harus<br>menjalankan fungsi|High|



|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|||validasi_real-time_<br>yang otomatis<br>menolak proses<br>simpan jika nomor<br>seri (_serial number_)<br>atau nomor aset yang<br>diinput Editor sudah<br>terdaftar di database,<br>guna mengeliminasi<br>risiko<br>ketidaksinkronan<br>data di pertengahan<br>tahun.||
|REQ-LOGIC-04|Sistem|Sistem harus memiliki<br>logika pemantauan<br>siklus hidup (_lifecycle_<br>_tracking_) yang<br>otomatis memberikan<br>tanda bendera merah<br>(_flagging_) pada<br>dasbor jika masa<br>berlaku kontrak<br>perangkat dengan<br>vendor atau masa<br>aktif lisensi software<br>tersisa kurang dari 30<br>hari.|Medium|
|REQ-LOGIC-05|Sistem|Sistem wajib<br>mengunci dokumen<br>berkas_Form Change_<br>_Request_(perubahan<br>fitur aplikasi) yang<br>diunggah oleh Editor<br>secara otomatis,<br>sehingga status<br>dokumen berubah<br>menjadi berkas<br>permanen yang tidak<br>dapat diedit kembali|Medium|



|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|||oleh siapa pun demi<br>menjaga validitas<br>data audit.||



## 4.2 Kebutuhan Data 

|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|REQ-DATA-01|Editor|Sistem WAJIB<br>menyediakan menu<br>_dropdown_Master<br>Data yang baku<br>untuk pengisian<br>formulir aset agar<br>terhindar dari<br>kesalahan ketik<br>(_typo_), meliputi:<br>Kategori Perangkat<br>(Laptop, Server,<br>Access Point), Versi<br>Office, Status Lisensi<br>Email, dan Lokasi<br>Penempatan Aset.|High|
|REQ-DATA-02|Sistem|Struktur basis data<br>aset (_Asset Register_)<br>harus menyediakan<br>field data terstruktur<br>yang wajib diisi<br>secara lengkap,<br>mencakup: Merek,<br>Nomor Seri, Nomor<br>Aset, Versi Microsoft<br>Office, Status Lisensi<br>Email, Nama<br>Pengguna Perangkat,<br>Lokasi Fisik, dan<br>Tanggal Perolehan|High|



|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|||Kontrak Vendor.||
|REQ-DATA-03|Editor|Sistem harus<br>menyediakan kolom<br>_upload_terpusat yang<br>menerima format file<br>PDF atau gambar<br>digital khusus untuk<br>berkas dokumen<br>administrasi teknis<br>seperti_Form Change_<br>_Request_perubahan<br>fitur aplikasi.|High|
|REQ-DATA-04|Viewer|Modul analitik WAJIB<br>menampilkan<br>komponen visual<br>berupa_Pie Chart_<br>untuk persentase<br>sebaran lokasi aset,<br>_Bar Chart_untuk total<br>jumlah aset per<br>kategori<br>(laptop/server/access<br>point), serta tabel<br>ringkasan lisensi<br>email yang aktif untuk<br>kemudahan<br>monitoring Manager|Medium|
|REQ-DATA-05|Editor|Sistem WAJIB<br>menyediakan fitur<br>Export Data ke dalam<br>format berkas Excel<br>(.xlsx) untuk seluruh<br>data Asset Register,<br>arsip Change<br>Request, dan<br>dokumen log Audit<br>Trail|High|



## 4.3 Kebutuhan Notifikasi 

|**Kode Req**|**Aktor**|**Deskripsi Kebutuhan**|**Prioritas**|
|---|---|---|---|
|REQ-NOTIF-01|Editor|Sistem wajib menampilkan<br>pesan konfirmasi pop-up<br>_"Data Aset Berhasil_<br>_Disimpan"_atau_"Dokumen_<br>_Berhasil Diarsip"_secara<br>instan di layar Editor setelah<br>aktivitas kirim data berhasil<br>diproses oleh database<br>terpusat.|High|
|REQ-NOTIF-02|Viewer|Dasbor monitoring<br>manajemen harus otomatis<br>menampilkan pesan<br>peringatan (_alert warning_) di<br>baris teratas jika ada lisensi<br>email perusahaan yang<br>statusnya mendekati<br>kedaluwarsa atau kontrak<br>sewa perangkat vendor<br>yang habis.|High|
|REQ-NOTIF-03|Viewer|Sistem harus memunculkan<br>indikator notifikasi merah<br>atau peringatan_real-time_<br>pada halaman utama<br>dasbor level Manager ke<br>atas setiap kali ada<br>dokumen_Form Change_<br>_Request_baru atau<br>pembaruan status aset kritis<br>yang dikirim oleh Editor.|Medium|



## 4. Kebutuhan Keamanan Sistem 

|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|REQ-AUTH-01|Semua User|Sistem**WAJIB**<br>menerapkan kontrol<br>akses berbasis peran<br>(_Role-Based Access_<br>_Control_/ RBAC) yang<br>secara mutlak<br>memisahkan hak<br>masuk dan<br>memblokir perimeter<br>menu Editor agar<br>tidak bisa diakses<br>oleh akun dengan<br>peran Viewer, begitu<br>pula sebaliknya.|High|
|REQ-AUTH-02|Semua User|Sistem harus<br>mengamankan<br>gerbang masuk<br>aplikasi dengan<br>mekanisme otentikasi<br>login standar yang<br>mewajibkan input<br>kombinasi_username_<br>(berupa email<br>perusahaan) dan<br>kode sandi<br>(_password_) yang<br>terenkripsi aman di<br>database.|High|
|REQ-AUTH-03|Semua User|Sistem**WAJIB**<br>mengaktifkan lapisan<br>keamanan tambahan<br>berupa Autentikasi<br>Dua Faktor<br>(2FA/MFA), di mana<br>pengguna harus<br>memasukkan kode<br>verifikasi sekunder<br>setelah_password_|High|



|**Kode Req**|**Aktor**|**Deskripsi**<br>**Kebutuhan**|**Prioritas**|
|---|---|---|---|
|||utama dinyatakan<br>benar sebelum<br>sistem memberikan<br>akses penuh.||
|REQ-AUTH-04|Admin IT|Sistem wajib<br>menyediakan modul<br>Pengelolaan<br>Pengguna (_User_<br>_Management_) khusus<br>bagi Admin IT untuk<br>menambah akun<br>baru, merubah status<br>peran (_Editor/Viewer_),<br>atau menonaktifkan<br>akun untuk<br>memfasilitasi rotasi<br>tim|Medium|



## BAB V: MATRIKS HAK AKSES 

## 5.1 Daftar Aktor (User Roles) 

|**Kode**|**Nama Peran**|**Deskripsi**|
|---|---|---|
|ROLE-01|**Editor**|Staf internal IT yang memiliki<br>hak akses penuh (_Full_<br>_Access_/CRUD) untuk<br>mengelola, menginput,<br>mengubah, dan<br>mengoperasikan keseluruhan<br>fungsi sistem.|
|ROLE-02|**Viewer/** **Read-Only (Level**<br>**Manager ke Atas)**|Jajaran manajemen mulai<br>dari level Manager ke atas<br>yang aksesnya hanya<br>sebatas melakukan monitor,<br>melihat data, melihat dasbor,<br>serta memeriksa dokumen<br>tanpa izin manipulasi data.|
|ROLE-03|**Admin IT**|Administrator sistem tingkat<br>akhir yang bertanggung<br>jawab mengelola akun<br>pengguna (_user_<br>_management_) serta mengatur<br>isi pilihan menu_dropdown_<br>(_master data_).|



## 5.2 Matriks Hak Akses — Modul CMDB Core (Asset Register & Lifecycle Tracking) 

|Tracking)||||
|---|---|---|---|
|**Fitur**|**Viewer**<br>|**Editor**<br>|**Admin IT**<br>|
|Pendaftaran Aset<br>Baru|❌<br>|C<br>✅<br>|❌<br>|
|Melihat Detail<br>Spesifikasi & Lokasi<br>(_Read_)|R<br>✅|R<br>✅|R<br>✅|



|**Fitur**|**Viewer**<br>|**Editor**<br>|**Admin IT**<br>|
|---|---|---|---|
|Pembaruan Data<br>Teknis & Lisensi<br>(_Update)_|❌<br>|U<br>✅<br>|❌<br>|
|Penghapusan Data<br>Perangkat (_Delete_)|❌|❌|✅D|



## 5.3 Matriks Hak Akses — Modul Formulir & Arsip Digital (Change Request) 

|**Fitur**|**Editor(Tim IT)**<br>|**Viewer ( Manager**<br>**Ke atas)**<br>|**Admin IT**<br>|
|---|---|---|---|
|Membuat Draf_Form_<br>_Change Request_|✅C<br>|❌<br>|❌<br>|
|Mengunggah<br>Dokumen<br>Administrasi|✅C<br>|❌<br>|❌<br>|
|Memonitor Status &<br>Melihat Arsip Berkas|✅R<br>|R<br>✅<br>|✅R<br>|
|Mengunci Berkas<br>secara Otomatis|✅U|❌|❌|



## 5.4 Matriks Hak Akses — Modul Dasbor Monitoring & Audit Trail 

|**Fitur**|**Editor(Tim IT)**<br>|**Viewer (Manager ke**<br>**atas)**<br>|**Admin IT**<br>|
|---|---|---|---|
|Melihat Dasbor Grafik<br>Pemantauan Aset|✅R<br>|✅**R**<br>|✅**R**<br>|
|Melihat Pesan<br>Peringatan (_Alert_) Lisensi|✅R<br>|✅**R**<br>|✅**R**<br>|
|Memeriksa Log Riwayat<br>Tahunan (_Audit Trail_)|✅R|✅**R**|✅**R**|



## 5.5 Matriks Hak Akses — Administrasi Sistem 

|**Fitur**|**Viewer**<br>|**Editor**<br>|**Admin IT**<br>|
|---|---|---|---|
|Kelola Akun<br>Pengguna (_User_<br>_Management_)|❌<br>|❌<br>|✅CRUD<br>|
|Kelola Pilihan Menu<br>_Dropdown_(_Master_<br>_Data_)|❌|❌|✅CRUD|



## 5.6 Keterangan Simbol 

|**Simbol**<br>|**Keterangan**|
|---|---|
|C<br>✅<br>|Create (Dapat membuat data baru)|
|R<br>✅<br>|Read (Dapat melihat data)|
|U<br>✅<br>|Update (Dapat mengubah data)|
|D<br>✅|Delete (Dapat menghapus data)|



|**Simbol**<br>|**Keterangan**|
|---|---|
|CRUD<br>✅<br>|Full Access (Create, Read, Update, Delete)|
|❌|Tidak memiliki akses|



## LAMPIRAN: GLOSARIUM 

|LAMPIRAN: GLOSARIUM||
|---|---|
|**Istilah**|**Definisi**|
|**CMDB**|_Configuration Management Database_—<br>Database terpusat yang digunakan untuk<br>mendata seluruh siklus hidup aset IT<br>perusahaan.|
|**Asset Register**|Daftar inventarisasi digital yang mencatat<br>informasi unit hardware (laptop, server,<br>_access point_) beserta lokasi penempatannya.|
|**Editor**|Peran pengguna khusus tim internal IT yang<br>memiliki otorisasi penuh untuk<br>mengoperasikan data pada keseluruhan<br>sistem.|
|**Viewer**|Peran pengguna khusus level Manager ke<br>atas dengan batasan hak akses baca untuk<br>fungsi monitoring.|
|**Audit Trail**|Fitur perekaman log otomatis yang mencatat<br>kronologi penambahan atau modifikasi data<br>aset per tahun untuk keperluan transparansi<br>audit.|
|**Change Request**|Formulir administrasi digital yang digunakan<br>untuk mendokumentasikan permohonan<br>perubahan fitur pada aplikasi perusahaan.|
|**Single Source of Truth**|Konsep arsitektur data di mana seluruh data<br>aset diintegrasikan ke dalam satu sumber<br>pangkalan data terpusat yang valid guna<br>mencegah ketidaksinkronan data.|



