# Setup Project Django - Test Junior Programmer FastPrint

Project ini dibuat menggunakan Django untuk memenuhi persyaratan test Junior Programmer di FastPrint.

## Persyaratan
- Python 3.10+
- XAMPP/MySQL
- Internet (untuk fetch data dari API)

## Langkah Instalasi

### 1. Persiapan Database
Pastikan MySQL di XAMPP sudah berjalan. Buat database baru dengan nama:
```sql
fastprint_test
```

### 2. Setup Virtual Environment
Buka terminal di root project dan jalankan:
```powershell
# Buat venv (sudah ada di folder jika Anda mengunduh project lengkap)
python -m venv venv

# Aktivasi venv
.\venv\Scripts\activate

# Install dependensi (Gunakan Django 4.2.19 untuk kompatibilitas MariaDB 10.4)
pip install django==4.2.19 djangorestframework mysqlclient requests
```

### 3. Migrasi Database
Jalankan perintah berikut untuk membuat tabel:
```powershell
python manage.py makemigrations produk
python manage.py migrate
```

### 4. Fetch Data dari API
Project ini memiliki management command untuk mengambil data dari API FastPrint secara otomatis:
```powershell
python manage.py fetch_data
```

### 5. Menjalankan Server
```powershell
python manage.py runserver
```
Akses di browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Fitur Project
- **Dashboard Produk**: Menampilkan semua produk dengan opsi filter status "bisa dijual".
- **CRUD**: Tambah, Edit, dan Hapus produk.
- **Validation**: Nama produk wajib diisi, harga wajib angka dan tidak boleh negatif.
- **REST Framework**: Menggunakan serializer untuk mapping data.
- **Auto-populate**: Kategori dan Status dibuat otomatis saat fetch data jika belum ada.

## Struktur Folder Penting
- `config/`: Konfigurasi utama Django dan Database MySQL.
- `produk/models.py`: Definisi tabel Produk, Kategori, dan Status.
- `produk/services.py`: Logic untuk integrasi API FastPrint.
- `produk/management/commands/`: Script console untuk otomasi fetch data.
- `produk/serializers.py`: Serializer untuk Django REST Framework.
- `produk/forms.py`: Validasi form produk.
