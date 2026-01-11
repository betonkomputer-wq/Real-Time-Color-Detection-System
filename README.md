# Real-Time-Color-Detection-System
Project ini membangun sistem deteksi warna berbasis kamera secara real time. Sistem mengenali objek berwarna merah, hijau, biru, dan kuning. Sistem menampilkan bounding box dan label warna langsung di layar. Project ini fokus pada computer vision dasar, pemrosesan citra, dan logika deteksi yang stabil.

FITUR UTAMA

Deteksi warna merah, hijau, biru, dan kuning

Pemrosesan video real time dari webcam

Bounding box otomatis pada objek terdeteksi

Label warna langsung pada objek

Noise reduction dengan Gaussian Blur dan morfologi

Tampilan sederhana dan responsif

TEKNOLOGI

Python

OpenCV

NumPy

CARA KERJA SISTEM

Kamera menangkap frame video secara real time

Sistem membalik frame agar interaksi lebih natural

Frame dikonversi ke ruang warna HSV

Sistem menerapkan threshold HSV untuk tiap warna

Mask dibersihkan dari noise menggunakan erosi dan dilasi

Kontur terbesar dengan area valid diproses

Sistem menggambar bounding box dan label warna

WARNA YANG DIDETEKSI

Merah dengan dua rentang HSV

Hijau dengan satu rentang HSV

Biru dengan satu rentang HSV

Kuning dengan satu rentang HSV

KONTROL

Tekan Q untuk keluar dari program

KEGUNAAN

Pembelajaran computer vision dasar

Dasar sistem tracking objek

Simulasi deteksi warna untuk robotika

Portofolio project image processing

CATATAN
Gunakan pencahayaan yang cukup agar deteksi stabil. Jarak kamera dan objek memengaruhi akurasi. Webcam standar sudah cukup untuk menjalankan sistem ini.
