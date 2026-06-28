import sys
import time

def teks_berjalan(teks, kecepatan_huruf=0.08, jeda_baris=1.5):
    """
    Fungsi untuk menampilkan teks berjalan per huruf.
    kecepatan_huruf: mengatur seberapa cepat huruf muncul (dalam detik)
    jeda_baris: mengatur jeda sebelum masuk ke baris lirik berikutnya (dalam detik)
    """
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()  # Memaksa terminal langsung menampilkan huruf
        time.sleep(kecepatan_huruf)
    print()  # Pindah ke baris baru setelah satu baris lirik selesai
    time.sleep(jeda_baris)

# Daftar lirik lagu dan pengaturannya
lirik = [
    ("🎵 (Hmmmm... yeah) 🎵", 0.1, 2.0),
    ("Terminal terbuka, layar berpijar...", 0.08, 1.5),
    ("Baris kode mengalir, menari liar...", 0.08, 1.5),
    ("Git push ke awan, jejak tersimpan...", 0.08, 1.5),
    ("Proyek ini hidup, takkan terlupakan. ✨", 0.09, 2.0)
]

print("=== MEMULAI PEMUTAR LIRIK ===")
time.sleep(1)

# Menjalankan lirik otomatis
for baris, kecepatan, jeda in lirik:
    teks_berjalan(baris, kecepatan, jeda)

print("\n=== LIRIK SELESAI ===")