from ultralytics import YOLO
import cv2

def analisis_foto_lokal(path_gambar):
    # Memuat model AI YOLOv8 (akan mengunduh model kecil sekali di awal)
    model = YOLO("yolov8n.pt") 

    # Menganalisis gambar
    results = model(path_gambar)

    # Menampilkan hasil deteksi di layar
    for result in results:
        result.show()  # Membuka jendela foto dengan kotak deteksi objek

if __name__ == "__main__":
    # Ganti dengan nama file gambar Anda
    path_gambar = "panji.jpg" 
    analisis_foto_lokal(path_gambar)