# 📘 Django POS API Project

Project ini merupakan implementasi pembelajaran Django dan Django REST Framework dari Modul 1 sampai Modul 7, mencakup pembuatan API, autentikasi, pagination, filter, serta import/export data.
link GDrive modul dan file csv 
https://drive.google.com/drive/folders/1W-AIb4M_Gg8ksKje9JirWIZWkt-3cXNl?usp=sharing
---

# 🚀 Modul 1 – Setup Project Django

* Membuat folder project
* Membuat virtual environment
* Aktivasi virtual environment
* Install Django
* Membuat project Django (`django-admin startproject`)
* Menjalankan server pertama (`runserver`)

---

# 🚀 Modul 2 – Membuat App

* Membuat app (`startapp`)
* Menambahkan app ke `INSTALLED_APPS`
* Struktur dasar Django (models, views, urls)
* Menjalankan migration awal

---

# 🚀 Modul 3 – Models & Database

* Membuat model:

  * StatusModel
  * JobTitle
* Menjalankan:

  * `makemigrations`
  * `migrate`
* Menggunakan Django shell:

  * Insert data
  * Query data (filter, exclude, get, count, exists)

---

# 🚀 Modul 4 – Relasi Antar Model

* Menggunakan ForeignKey
* Relasi antar tabel
* Query relasi:

  * `status__id`
  * join antar model
* Iterasi data menggunakan ORM

---

# 🚀 Modul 5 – Django REST Framework (API)

* Install Django REST Framework
* Menambahkan ke `INSTALLED_APPS`
* Membuat serializer
* Membuat API:

  * GET
  * POST
  * PUT
  * DELETE
* Testing API menggunakan Postman/Insomnia

---

# 🚀 Modul 6 – Authentication (Token)

* Register API
* Login API
* Generate token
* Menggunakan TokenAuthentication
* Proteksi endpoint dengan:

  * `IsAuthenticated`
* Menggunakan header:

  ```
  Authorization: Token <your_token>
  ```

---

# 🚀 Modul 7 – Pagination & Filter

### Pagination

* Menggunakan `LimitOffsetPagination`
* Konfigurasi di `settings.py`
* Membuat custom pagination

### Filter

* Install `django-filter`
* Menambahkan filter backend
* Filtering data:

  * berdasarkan kategori
* Menggunakan query:

  ```
  ?limit=10&offset=0
  ?category__name=Makanan
  ```

---

# 🚀 Modul Tambahan – Import Export Data

* Install:

  ```
  django-import-export
  ```
* Konfigurasi di `INSTALLED_APPS`
* Menggunakan `ImportExportModelAdmin`
* Import data CSV melalui Django Admin

---

# 🖼️ Image Handling

* Menggunakan `ImageField`
* Konfigurasi:

  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```
* Menyimpan file gambar di:

  ```
  media/menu_images/
  ```
* Path gambar di CSV:

  ```
  menu_images/nama_file.jpg
  ```

---

# ⚠️ Catatan Penting

* Field `created_on` dan `last_modified` otomatis, tapi ketika import CSV di komentarin dlu
* ForeignKey menggunakan ID (bukan nama)
* Nama file gambar harus sesuai dengan file di folder media

---

# 📡 Endpoint API

* Register: `/api/register`
* Login: `/api/login`
* Menu: `/api/menu-resto`
* Menu Filter: `/api/menu-resto-filter`

---

# 🛠️ Tools

* Django
* Django REST Framework
* django-filter
* django-import-export
* Postman / Insomnia

---

