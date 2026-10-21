import cv2

def analisis_dasar_foto(path_gambar):
    # Membaca gambar
    img = cv2.imread(path_gambar)
    
    if img is None:
        print("Error: Gambar tidak ditemukan!")
        return

    # Mengambil resolusi dan jumlah channel warna
    tinggi, lebar, saluran = img.shape
    
    print("--- HASIL ANALISIS DASAR ---")
    print(f"Lebar Gambar : {lebar} pixel")
    print(f"Tinggi Gambar: {tinggi} pixel")
    print(f"Total Pixel  : {lebar * tinggi}")

if __name__ == "__main__":
    analisis_dasar_foto("panji.jpg")