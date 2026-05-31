# Analisis Persepsi Audiens YouTube Menggunakan NLP dan Analisis Sentimen

## Demo Aplikasi

Aplikasi dapat diakses secara publik melalui Hugging Face Spaces:

https://huggingface.co/spaces/myu9s/dashboard

---

## Deskripsi Proyek

Proyek ini merupakan sistem analisis persepsi audiens berbasis Natural Language Processing (NLP) yang dirancang untuk menganalisis hubungan antara isi sebuah video YouTube dengan respons audiens yang disampaikan melalui kolom komentar.

Sistem secara otomatis mengambil komentar YouTube, melakukan transkripsi audio video menjadi teks, menganalisis sentimen isi video dan komentar, kemudian mengukur tingkat kesesuaian persepsi antara pesan yang disampaikan pembuat konten dengan tanggapan audiens.

Hasil analisis kemudian divisualisasikan dalam bentuk dashboard interaktif yang dapat diakses secara online.

---

## Latar Belakang

YouTube merupakan salah satu platform media sosial terbesar yang menghasilkan jutaan komentar setiap hari. Komentar-komentar tersebut mencerminkan persepsi, opini, dan respons audiens terhadap suatu konten.

Namun, melakukan analisis secara manual terhadap ribuan komentar memerlukan waktu yang lama dan sulit dilakukan secara konsisten.

Melalui pemanfaatan NLP dan Machine Learning, proses analisis sentimen dapat dilakukan secara otomatis sehingga dapat membantu memahami:

* Persepsi audiens terhadap suatu video.
* Kesesuaian antara isi video dan tanggapan audiens.
* Dominasi sentimen yang muncul pada suatu topik.
* Relevansi komentar terhadap isi video.

---

## Tujuan Proyek

* Mengambil komentar dari video YouTube secara otomatis.
* Mengubah audio video menjadi teks menggunakan Speech-to-Text.
* Melakukan analisis sentimen terhadap komentar audiens.
* Melakukan analisis sentimen terhadap isi video.
* Mengukur tingkat kesesuaian persepsi antara video dan komentar.
* Menyajikan hasil analisis dalam dashboard interaktif.

---

## Alur Sistem

```text
Video YouTube
      │
      ▼
Pengambilan Komentar
(YouTube Data API)
      │
      ▼
Ekstraksi Audio Video
(yt-dlp)
      │
      ▼
Transkripsi Audio
(OpenAI Whisper)
      │
      ▼
Preprocessing Teks
      │
      ▼
Analisis Sentimen
(Indonesian RoBERTa)
      │
      ▼
Analisis Similarity
      │
      ▼
Visualisasi Dashboard
(Streamlit)
```

---

## Fitur Utama

### 1. Pengambilan Komentar YouTube

Sistem mengambil data komentar menggunakan YouTube Data API yang meliputi:

* Isi komentar
* Nama pengguna
* Tanggal komentar
* Jumlah likes

---

### 2. Transkripsi Otomatis Video

Audio video diunduh menggunakan yt-dlp kemudian ditranskripsikan menjadi teks menggunakan model OpenAI Whisper.

---

### 3. Preprocessing Teks Bahasa Indonesia

Tahapan preprocessing meliputi:

* Case Folding
* Penghapusan URL
* Penghapusan HTML Tag
* Penghapusan Emoji
* Penghapusan Angka
* Normalisasi Kata Slang
* Pembersihan Karakter Khusus

---

### 4. Analisis Sentimen

Setiap komentar diklasifikasikan ke dalam tiga kategori:

* Positif
* Netral
* Negatif

Menggunakan model:

```text
w11wo/indonesian-roberta-base-sentiment-classifier
```

---

### 5. Rule-Based Sentiment Refinement

Untuk meningkatkan kualitas klasifikasi, sistem menambahkan aturan berbasis kata kunci positif dan negatif yang umum digunakan dalam komentar berbahasa Indonesia.

---

### 6. Analisis Sentimen Transkrip Video

Transkrip video dipecah menjadi beberapa kalimat kemudian setiap kalimat dianalisis sentimennya untuk menentukan sentimen dominan video.

---

### 7. Analisis Kesesuaian Persepsi

Proyek ini tidak hanya menganalisis sentimen komentar, tetapi juga membandingkan sentimen video dan komentar untuk mengetahui apakah persepsi audiens sesuai dengan pesan yang disampaikan dalam video.

Output yang dihasilkan:

* Sentimen Dominan Video
* Sentimen Dominan Komentar
* Status Kesesuaian Persepsi
* Similarity Score

---

### 8. Analisis Kemiripan Kontekstual

Menggunakan model:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

Untuk menghitung:

* Cosine Similarity
* Tingkat kemiripan konteks antara isi video dan komentar

---

### 9. Dashboard Interaktif

Dashboard menampilkan:

* Total komentar
* Distribusi sentimen
* Rasio sentimen negatif
* Filter komentar berdasarkan sentimen
* Tabel komentar hasil preprocessing

---

## Teknologi yang Digunakan

### Bahasa Pemrograman

* Python

### NLP & Machine Learning

* Transformers
* Hugging Face
* Indonesian RoBERTa
* Sentence Transformers
* OpenAI Whisper

### Pengolahan Data

* Pandas
* NumPy

### Visualisasi

* Matplotlib
* Seaborn
* WordCloud

### Dashboard

* Streamlit

### Deployment

* Hugging Face Spaces

### API

* YouTube Data API v3

---

## Model yang Digunakan

### Analisis Sentimen

Model:

```text
w11wo/indonesian-roberta-base-sentiment-classifier
```

Fungsi:

* Klasifikasi Sentimen Positif
* Klasifikasi Sentimen Netral
* Klasifikasi Sentimen Negatif

---

### Semantic Similarity

Model:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

Fungsi:

* Mengukur kemiripan konteks antara isi video dan komentar audiens.

---

### Speech Recognition

Model:

```text
OpenAI Whisper
```

Fungsi:

* Mengubah audio video menjadi teks secara otomatis.

---

## Evaluasi Model

Evaluasi dilakukan menggunakan:

* Manual Labeling
* Accuracy Score
* Confusion Matrix

Hasil evaluasi menunjukkan model mampu melakukan klasifikasi sentimen dengan performa yang cukup baik pada data komentar berbahasa Indonesia.

---

## Hasil yang Diperoleh

Melalui proyek ini dapat diketahui:

* Sentimen dominan audiens terhadap suatu video.
* Sentimen dominan isi video.
* Tingkat kesesuaian persepsi antara pembuat konten dan audiens.
* Kemiripan konteks antara video dan komentar.
* Topik yang paling sering dibahas dalam komentar.

---

## Pengembangan Selanjutnya

* Analisis sentimen real-time berdasarkan URL video.
* Aspect-Based Sentiment Analysis.
* Topic Modeling.
* Ringkasan otomatis menggunakan Large Language Model (LLM).
* Visualisasi yang lebih interaktif menggunakan Plotly.
* Dukungan multi-bahasa.

---

## Author

**Mochammad Yuga Ranapraja**

Mahasiswa Informatika
Junior Data Science Intern at Vinix7

---

## Kompetensi yang Ditunjukkan

* Natural Language Processing (NLP)
* Machine Learning
* Deep Learning
* Sentiment Analysis
* Speech Recognition
* Data Mining
* Data Visualization
* Streamlit Development
* Hugging Face Deployment
* API Integration
* Model Evaluation
* Semantic Similarity Analysis
