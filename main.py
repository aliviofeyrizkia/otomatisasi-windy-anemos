from img_scraper import img_scraper
import cv2
import csv
from datetime import datetime

# 1. URL target (misalnya peta Windy dengan parameter hujan)
url = "https://www.windy.com/-6.935/107.606/gfs?gfs,rh,-7.331,107.606,9,m:dtBai8v"  # Contoh Bandung
date = datetime.utcnow().strftime("%Y%m%d_%H%M")

# 2. Ambil screenshot Windy
img_scraper(url, "windy.png")

# 3. Baca screenshot
img = cv2.imread("windy.png")

# Tentukan pixel koordinat (ditentukan manual pakai color_checker.py)
x, y = 600, 400
b, g, r = img[y, x]
print(f"Pixel RGB: {r},{g},{b}")

# 4. Klasifikasi sederhana
if b > 200 and g < 100:
    kategori = "Hujan Tinggi"
elif b > 150:
    kategori = "Hujan Sedang"
elif b > 50:
    kategori = "Hujan Ringan"
else:
    kategori = "Tidak Hujan"

print("Kategori:", kategori)

# 5. Simpan hasil ke CSV
row = [date, r, g, b, kategori]
with open("hasil_windy.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)
