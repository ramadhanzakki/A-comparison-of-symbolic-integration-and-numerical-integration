import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk memebuat persamaan matematika non-trivial dan menghitung anti-turunanya dengan cara simbolik
def integrasi_simbolik():
    # Inisialisasi variabel simbolik
    print('     [STATUS] -> Inisialisasi varaibel simbolik')
    x = sp.Symbol('x')

    # Inisialisasi fungsi non-trivial f(x) = x * e(-x^2)
    print('     [STATUS] -> Inisialisasi fungsi non-trivial')
    f_x = x * sp.exp(-x**2)

    # Perhitungan anti-turunan dengan cara sombolik
    print('     [STATUS] -> Melakukan perhitungan anti-turunan dengan metode simbolik')
    F_x = sp.integrate(f_x, x)

    return x, f_x, F_x

# Fungsi untuk mengkonversi simbolik ke numerik dan menampilkan visualisasi grafik
def visualisasikan_grafik(x, f_x, F_x):
    # Konversi ekspresi simbolik ke fungsi numerik
    f_num = sp.lambdify(x, f_x, 'numpy')
    F_num = sp.lambdify(x, F_x, 'numpy')
    
    # Generasi array titik data x (domain: -3 sampai 3)
    x_vals = np.linspace(-3, 3, 500)
    y_f = f_num(x_vals)
    y_F = F_num(x_vals)
    
    # Pembuatan canvas dan plot grafik
    plt.figure(figsize=(10, 6))
    
    # Plot kurva f(x) dan F(x)
    plt.plot(x_vals, y_f, label=f'$f(x) = {sp.latex(f_x)}$ (Fungsi Asli)', color='blue', linewidth=2)
    plt.plot(x_vals, y_F, label=f'$F(x) = {sp.latex(F_x)}$ (Hasil Integrasi)', color='red', linestyle='--', linewidth=2)
    
    # Arsir daerah di bawah kurva f(x) pada interval [0, 1.5] (visualisasi daerah integrasi)
    x_fill = np.linspace(0, 1.5, 100)
    plt.fill_between(x_fill, f_num(x_fill), color='skyblue', alpha=0.4, label='Area Integral Tentu [0, 1.5]')
    
    # Formatting properti grafik
    plt.title('Integrasi Simbolik dan Visualisasi Model Matematika', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sumbu X', fontsize=11)
    plt.ylabel('Sumbu Y', fontsize=11)
    plt.axhline(0, color='black', linewidth=0.8, linestyle=':')  # Garis x=0
    plt.axvline(0, color='black', linewidth=0.8, linestyle=':')  # Garis y=0
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10, loc='upper right')
    
    # Simpan hasil grafik untuk dimasukkan ke laporan Word/PDF
    plt.savefig('visualisasi_integrasi.png', dpi=300, bbox_inches='tight')
    print("[INFO] Grafik berhasil disimpan sebagai 'visualisasi_integrasi.png'")
    
    # Tampilkan grafik
    plt.show()

def main():
    print('=== PROGRAM INTEGRASI SIMBOLIK ===')

    print('[STATUS] -> Menjalankan perhitungan simbolik')
    x, f_x, F_x = integrasi_simbolik()
    print('[STATUS] -> Perhitungan berhasil')

    print('\n[STATUS] -> Menampilkan hasil perhitungan')
    print(f'    [RESULT] -> Fungsi asli      f(x): {f_x}')
    print(f'    [RESULT] -> Fungsi simbolik  f(x): {F_x} + C\n')

    visualisasikan_grafik(x, f_x, F_x)

if __name__ == "__main__":
    main()