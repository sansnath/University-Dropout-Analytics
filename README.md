# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Institusi pendidikan ini menghadapi tantangan serius berupa **tingginya tingkat dropout (putus studi)** di kalangan mahasiswa.  
Masalah ini berdampak pada penurunan tingkat kelulusan, meningkatnya beban administratif, serta berkurangnya efisiensi sumber daya akademik.

Departemen akademik membutuhkan **dashboard analitik berbasis Metabase** untuk memahami faktor-faktor utama penyebab dropout.  
Dengan demikian, kebijakan peningkatan retensi mahasiswa dapat dirancang secara **berbasis data (data-driven decision making)**.

### Permasalahan Bisnis

- Tingginya tingkat dropout mahasiswa (sekitar **32,12%** dari total populasi).  

- Dropout didominasi oleh **mahasiswa berkewarganegaraan Portugis**.  

- **Kurangnya dukungan beasiswa** menjadi faktor kuat penyebab dropout.

- **Nilai akademik rendah** pada dua semester awal sangat berkorelasi dengan dropout.

- Mahasiswa **berusia lebih tua saat pendaftaran** lebih berisiko tidak menyelesaikan studi.

- Program studi seperti **Management (Evening)** dan **Nursing** memiliki dropout tertinggi.  

### Cakupan Proyek

- Melakukan **analisis faktor dropout mahasiswa** berdasarkan data pendidikan tinggi.

- Membangun **dashboard Metabase** untuk memvisualisasikan dropout berdasarkan faktor demografis, finansial, dan akademik.

- Mengembangkan **model prediktif (XgBoost)** untuk memperkirakan kemungkinan dropout.  

- Menyusun **rekomendasi kebijakan berbasis data** guna menurunkan tingkat dropout.


### Persiapan
1. Sumber data: Education Dataset (https://drive.google.com/file/d/1hfXQbYuWfJ2E_1TMVu5ebYOnYhXxGR0C/view?usp=sharing)
Gunakan akun berikut untuk login ke Metabase:
- Email/Username:
- Password:
  
2. Membuat dan Mengaktifkan Virtual Environment
Linux / MacOS
python3 -m venv venv
source venv/bin/activate

Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

3. Menginstal Dependensi
Instal semua dependensi dari requirements.txt:
pip install -r requirements.txt

## Cara Menjalankan Metabase
1. Jalankan container metabase:
   ```bash
   docker run -d -p 3000:3000 \
     -v $(pwd)/metabase_education_export.mv.db:/metabase.db/metabase.db.mv.db \
      --name metabase_education metabase/metabase

## Cara Menjalankan Script Python
streamlit run app.py

## Menjalankan Sistem Machine Learning
1. Struktur Folder
Pastikan struktur direktori seperti berikut:
project/
├── model/
│ ├── best_xgb_model.joblib 
│ ├── important_features.pkl 
│ ├── pca_model.pkl 
│ └── scaler.pkl 
├── app.py # 
├── requirement.txt 
├── README.md
2. Menginstal Dependensi
Instal semua dependensi dari requirements.txt:
pip install -r requirements.txt
3. Menjalankan Aplikasi Streamlit
Untuk memulai antarmuka prediksi:
streamlit run app.py

## Business Dashboard

Dashboard dibuat menggunakan Metabase, dengan fokus utama:
- Dropout berdasarkan Kewarganegaraan
- Dropout berdasarkan Status Beasiswa & Debitur
- Dropout berdasarkan Nilai 2 Semester Awal
- Dropout berdasarkan Usia Saat Pendaftaran
- Dropout berdasarkan Program Studi

Dashboard ini membantu pihak kampus untuk:
- Mengidentifikasi kelompok mahasiswa dengan risiko dropout tertinggi.
- Menemukan faktor akademik dan finansial yang paling memengaruhi dropout.
- Memberikan insight cepat untuk kebijakan dukungan mahasiswa.

## Conclusion

- Tingkat dropout: 32,12%
- Faktor dominan: Kewarganegaraan Portugis dan dukungan finansial
- Prediktor utama: Nilai akademik rendah di awal studi
- Kelompok berisiko tinggi: Mahasiswa lebih tua dan berstatus debitur
- Program studi perlu perhatian: Management (Evening), Nursing

### Rekomendasi Action Items (Optional)

1. Kewarganegaraan & Usia

- Mayoritas dropout berasal dari mahasiswa Portugis berusia lebih tua.
- Buat program orientasi dan dukungan akademik cepat (fast-track) khusus untuk kelompok ini.

2. Dukungan Finansial

- Tidak adanya beasiswa dan status debitur memperbesar risiko dropout.
- Perluas program beasiswa dan bantuan finansial bagi kelompok berisiko tinggi.

3. Kinerja Akademik Dini

- Nilai rendah di dua semester awal menunjukkan adaptasi akademik yang lemah.
- Terapkan Early Warning System (EWS) berbasis nilai semester pertama dan program remediasi wajib bagi mahasiswa dengan GPA < 8.0.

4. Program Studi Berisiko

- Program seperti Management (Evening) dan Nursing memiliki tingkat dropout tertinggi.
- Lakukan evaluasi kurikulum dan beban studi, serta berikan dukungan akademik tambahan untuk mahasiswa program tersebut.
