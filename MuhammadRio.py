1.	Machine learning (ML) adalah cabang dari kecerdasan buatan (Artificial Intelligence, AI) yang memungkinkan sistem untuk belajar dan meningkatkan kinerjanya secara otomatis dari pengalaman tanpa perlu diprogram secara eksplisit. Dalam machine learning, algoritma digunakan untuk menganalisis data, mengenali pola, dan membuat keputusan atau prediksi berdasarkan data tersebut.



2.	Machine learning telah diimplementasikan dalam berbagai aspek kehidupan sehari-hari, membantu meningkatkan efisiensi, akurasi, dan kenyamanan dalam banyak bidang. Berikut adalah beberapa contoh penerapannya:

-	Rekomendasi Produk (E-commerce)
a.	Penerapan: Platform seperti Amazon, Netflix, dan Spotify menggunakan machine learning untuk merekomendasikan produk, film, atau lagu kepada pengguna berdasarkan riwayat pencarian dan pembelian mereka.
b.	Mengapa Diperlukan: Membantu pengguna menemukan produk atau konten yang relevan dengan cepat tanpa harus mencarinya secara manual.
c.	Manfaat: Meningkatkan pengalaman pengguna dan mendorong peningkatan penjualan atau penggunaan platform.
-	Pengenalan Wajah (Face Recognition)
d.	Penerapan: Teknologi pengenalan wajah digunakan di smartphone untuk membuka kunci perangkat, di bandara untuk keamanan, dan di media sosial untuk menandai foto.
e.	Mengapa Diperlukan: Menyediakan cara yang cepat dan aman untuk mengidentifikasi individu.
f.	Manfaat: Meningkatkan keamanan dan kenyamanan pengguna.
-	Asisten Virtual (Virtual Assistants)
g.	Penerapan: Asisten virtual seperti Siri, Google Assistant, dan Alexa menggunakan machine learning untuk memahami dan menanggapi perintah suara pengguna.
h.	Mengapa Diperlukan: Mempermudah interaksi pengguna dengan teknologi melalui perintah suara.
i.	Manfaat: Meningkatkan produktivitas dan kenyamanan, memungkinkan pengguna untuk melakukan berbagai tugas dengan lebih efisien.




3.	Dalam penerapan machine learning, terdapat berbagai macam pendekatan yang dapat dikategorikan ke dalam beberapa taxonomi utama. Taxonomi ini membantu mengklasifikasikan jenis-jenis machine learning berdasarkan metode pembelajaran dan tipe masalah yang dihadapi. Berikut adalah beberapa taxonomi utama dalam machine learning:
-	Supervised Learning (Pembelajaran Terawasi)
•	Definisi: Algoritma belajar dari dataset yang diberi label, yaitu setiap data input memiliki output yang diketahui.
•	Contoh Penerapan: Klasifikasi email sebagai spam atau bukan spam, prediksi harga rumah berdasarkan fitur-fitur tertentu.
•	Algoritma Populer: Linear Regression, Logistic Regression, Decision Trees, Support Vector Machines (SVM), Neural Networks.
-	Unsupervised Learning (Pembelajaran Tak Terawasi)
•	Definisi: Algoritma belajar dari dataset yang tidak diberi label dan berusaha menemukan struktur atau pola dalam data.
•	Contoh Penerapan: Segmentasi pelanggan, pengelompokan dokumen berdasarkan topik.
•	Algoritma Populer: K-Means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA), Association Rules.
2.	Semi-Supervised Learning (Pembelajaran Semi-Terawasi)
•	Definisi: Kombinasi dari supervised dan unsupervised learning. Algoritma dilatih menggunakan dataset yang sebagian besar tidak diberi label dan sebagian kecil diberi label.
•	Contoh Penerapan: Klasifikasi gambar di mana hanya sebagian kecil gambar yang diberi label.
•	Algoritma Populer: Semi-Supervised SVM, Self-Training, Co-Training.

Studi Kasus. 
1. a) Berapa rata-rata mahasiswa datang pada minggu ini?
Rata-rata mahasiswa datang pada minggu ini adalah 3.2 orang per hari. Rata-rata = Total datang / Total hari = 19 / 7 = 3.2 orang per hari
b) Kapan biaya tertinggi terjadi?
Biaya tertinggi terjadi pada hari Sabtu, dengan total biaya Rp 150.000.
c) Hari apa biaya lebih dari 110000?
Biaya lebih dari 110.000 terjadi pada hari Selasa dan Sabtu.
d) Siapa yang paling banyak datang ke kampus?
Ani paling banyak datang ke kampus, dengan total 11 hari.
e) Siapa yang datang pada hari Minggu?
Ani dan Budi datang pada hari Minggu.
f) Berapa biaya tertinggi dan terendah?
Biaya tertinggi adalah Rp 150.000 pada hari Sabtu, dan biaya terendah adalah Rp 15.000 pada hari Kamis.
g) Berapa frekuensi datang tertinggi dan terendah?
Frekuensi datang tertinggi adalah 5 kali, terjadi pada Ani pada hari Sabtu.
Frekuensi datang terendah adalah 1 kali, terjadi pada Lono pada hari Kamis.


2. import pandas as pd
import matplotlib.pyplot as plt

# Define the data
fakultas = ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"]
jumlah_mahasiswa = [260, 28, 284, 465, 735]
akreditasi = ["A", "A", "B", "A", "A"]

# Create a DataFrame
info_mahasiswa = pd.DataFrame({
    'fakultas': fakultas,
    'jumlah_mahasiswa': jumlah_mahasiswa,
    'akreditasi': akreditasi
})

# Plot the data
plt.figure(figsize=(10, 6))
bars = plt.bar(info_mahasiswa['fakultas'], info_mahasiswa['jumlah_mahasiswa'], color=['red', 'green', 'blue', 'cyan', 'magenta'])

# Adding labels and title
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')

# Adding a legend
plt.legend(bars, fakultas)

# Show the plot
plt.show()    
