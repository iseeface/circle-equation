import matplotlib.pyplot as plt
import numpy as np

def persamaan_lingkaran(a, b, r):
    # Menghasilkan persamaan lingkaran
    return f"(x - {a})^2 + (y - {b})^2 = {r**2}"

def draw_circle(a, b, r, persamaan):
    # Membuat data untuk lingkaran
    theta = np.linspace(0, 2 * np.pi, 100)  # Sudut dari 0 hingga 2π
    x = a + r * np.cos(theta)  # Koordinat x
    y = b + r * np.sin(theta)  # Koordinat y

    # Menggambar lingkaran
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f'Lingkaran: Pusat({a}, {b}), Jari-jari {r}')
    plt.scatter(a, b, color='red')  # Titik pusat
    plt.text(a, b, f' Pusat({a}, {b})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    
    # Menambahkan persamaan lingkaran di bawah gambar
    plt.text(a, b - r - 2, persamaan, fontsize=12, ha='center', va='top', color='blue')

    # Mengatur batas dan aspek
    plt.xlim(a - r - 1, a + r + 1)
    plt.ylim(b - r - 1, b + r + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title('Lingkaran')
    plt.legend()
    plt.show()

# Nilai tetap untuk a, b, dan r
a = 5  # Koordinat x pusat
b = 9  # Koordinat y pusat
r = 10  # Jari-jari lingkaran

# Mendapatkan dan mencetak persamaan lingkaran
persamaan = persamaan_lingkaran(a, b, r)
print("Persamaan lingkaran:", persamaan)

# Menggambar lingkaran
draw_circle(a, b, r, persamaan)
