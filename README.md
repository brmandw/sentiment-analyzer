# Flask AI Mini Web App

Proyek ini adalah aplikasi web sederhana menggunakan Flask dan Python, yang terhubung ke layanan AI (seperti Google Generative AI).

## 🔧 Fitur

- Input teks melalui antarmuka web
- Analisis teks menggunakan AI
- Output ditampilkan ke halaman

## 🚀 Cara Menjalankan

1. **Clone repositori:**
   <bash>
   git clone https://github.com/username/nama-proyek.git
   cd nama-proyek
   
3. **Buat dan aktifkan virtual environment:**
   <bash>
   python3 -m venv venv
   source venv/bin/activate

5. **Install dependency:**
   <bash>
   pip install -r requirements.txt

7. **Buat file .env:**
   <env>
   SENTIMENTANALYZER_API_KEY=masukkan_api_kamu_di_sini
   FLASK_APP=main.py
   FLASK_ENV=development

9. **Jalankan Flask:**
    <bash>
   flask run
   
Aplikasi akan berjalan di http://127.0.0.1:5000/
