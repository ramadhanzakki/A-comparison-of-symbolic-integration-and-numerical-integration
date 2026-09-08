# Perbandingan Integrasi Simbolik dan Numerik

Program Python sederhana untuk menghitung anti-turunan (integral tak tentu) suatu fungsi secara simbolik dan memvisualisasikan hasilnya secara numerik ke dalam bentuk grafik.

---

## Fungsi Matematika yang Digunakan

Program ini menggunakan fungsi non-trivial:

- **Fungsi Asli:**
  $$f(x) = x \cdot e^{-x^2}$$

- **Hasil Integrasi Simbolik (Anti-turunan):**
  $$F(x) = \int x \cdot e^{-x^2} \, dx = -\frac{1}{2} e^{-x^2} + C$$

- **Domain dan Batas Area:**
  - Domain visualisasi: $x \in [-3, 3]$
  - Area integral tentu yang divisualisasikan (arsiran): interval $[0, 1.5]$

---

## Kesimpulan

1. **Kemampuan CAS dalam Integrasi Simbolik**  
   Penggunaan pustaka `sympy` sebagai *Computer Algebra System* (CAS) terbukti dapat menyelesaikan persamaan integral non-trivial $f(x) = x \cdot e^{-x^2}$ secara simbolik/aljabar murni menghasilkan anti-turunan persis $F(x) = -\frac{e^{-x^2}}{2} + C$, bukan sekadar menghitung nilai aproksimasi numerik.

2. **Hubungan Visual $f(x)$ dan $F(x)$**  
   Melalui grafik Matplotlib, terlihat jelas hubungan matematis antara fungsi asli $f(x)$ dan hasil integrasinya $F(x)$:
   - Titik di mana $f(x) = 0$ (pada $x = 0$) bertepatan dengan titik stasioner (nilai ekstrem/puncak) dari fungsi anti-turunan $F(x)$.
   - Luas daerah yang diarsir pada interval $[0, 1.5]$ merepresentasikan nilai integral tentu $\int_{0}^{1.5} f(x) \, dx$.

3. **Efisiensi Integrasi Simbolik-Numerik**  
   Fungsi `sp.lambdify` berhasil menjembatani komputasi simbolik (SymPy) dan komputasi numerik (NumPy/Matplotlib), sehingga ekspresi aljabar kompleks dapat dievaluasi pada ratusan titik data secara efisien dan menghasilkan kurva visualisasi yang mulus.

---

## Library yang Digunakan

Program ini dibangun menggunakan beberapa library Python:

1. **[SymPy](https://www.sympy.org/) (`sympy`)**  
   Digunakan untuk komputasi matematika simbolik: mendefinisikan variabel simbolik, menghitung integral secara analitis/simbolik (`sp.integrate`), dan mengonversi fungsi simbolik menjadi fungsi numerik (`sp.lambdify`).
2. **[NumPy](https://numpy.org/) (`numpy`)**  
   Digunakan untuk komputasi numerik: membuat array titik data $x$ (`np.linspace`) untuk dievaluasi oleh fungsi.
3. **[Matplotlib](https://matplotlib.org/) (`matplotlib.pyplot`)**  
   Digunakan untuk visualisasi grafik: memplot kurva $f(x)$, kurva $F(x)$, mengarsir area di bawah kurva, dan menyimpan visualisasi ke file gambar.

---

## Cara Menjalankan Program

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
