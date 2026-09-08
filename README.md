# Perbandingan Integrasi Simbolik dan Numerik

Program Python sederhana untuk menghitung anti-turunan (integral tak tentu) suatu fungsi secara simbolik dan memvisualisasikan hasilnya secara numerik ke dalam bentuk grafik.

---

## 📐 Fungsi Matematika yang Digunakan

Program ini menggunakan fungsi non-trivial:

- **Fungsi Asli:**
  $$f(x) = x \cdot e^{-x^2}$$

- **Hasil Integrasi Simbolik (Anti-turunan):**
  $$F(x) = \int x \cdot e^{-x^2} \, dx = -\frac{1}{2} e^{-x^2} + C$$

- **Domain dan Batas Area:**
  - Domain visualisasi: $x \in [-3, 3]$
  - Area integral tentu yang divisualisasikan (arsiran): interval $[0, 1.5]$

---

## 📦 Library yang Digunakan

Program ini dibangun menggunakan beberapa library Python:

1. **[SymPy](https://www.sympy.org/) (`sympy`)**  
   Digunakan untuk komputasi matematika simbolik: mendefinisikan variabel simbolik, menghitung integral secara analitis/simbolik (`sp.integrate`), dan mengonversi fungsi simbolik menjadi fungsi numerik (`sp.lambdify`).
2. **[NumPy](https://numpy.org/) (`numpy`)**  
   Digunakan untuk komputasi numerik: membuat array titik data $x$ (`np.linspace`) untuk dievaluasi oleh fungsi.
3. **[Matplotlib](https://matplotlib.org/) (`matplotlib.pyplot`)**  
   Digunakan untuk visualisasi grafik: memplot kurva $f(x)$, kurva $F(x)$, mengarsir area di bawah kurva, dan menyimpan visualisasi ke file gambar.

---

## 🚀 Cara Menjalankan Program

1. **Prasyarat**: Pastikan Python sudah terinstal.
2. **Instal dependensi:**
   ```bash
   pip install sympy numpy matplotlib
   ```
3. **Jalankan program:**
   ```bash
   python main.py
   ```

---

## 📊 Output Program

- **Terminal:** Menampilkan proses inisialisasi, fungsi asli, dan ekspresi simbolik hasil integrasi.
- **File Gambar:** Grafik otomatis disimpan sebagai `visualisasi_integrasi.png` dengan resolusi tinggi (300 DPI) dan ditampilkan di layar.
