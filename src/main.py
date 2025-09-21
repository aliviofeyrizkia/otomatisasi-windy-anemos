import pandas as pd
from ocr_utils import crop_and_ocr
from windy_scraper import capture_windy_screenshot

def main():
    # Step 1: Ambil screenshot dari Windy
    url = "https://www.windy.com/-6.935/107.606/gfs?gfs,rh,-7.331,107.606,9,m:dtBai8v"  # bisa ganti ke layer forecast/hujan
    image_path = capture_windy_screenshot(url, save_path="windy.png")

    # Step 2: Crop & OCR untuk beberapa kolom
    # (contoh koordinat, perlu disesuaikan dengan tampilan asli Windy di screenshot)
    coords = {
        "Date": (100, 200, 200, 800),
        "Temp": (250, 200, 350, 800),
        "Rain": (400, 200, 500, 800),
    }

    dfs = []
    for col, crop in coords.items():
        df = crop_and_ocr(image_path, crop, col)
        dfs.append(df)

    # Step 3: Gabungkan semua kolom ke 1 tabel
    final_df = pd.concat(dfs, axis=1)

    # Step 4: Simpan ke CSV
    output_path = "data/windy_parsed.csv"
    final_df.to_csv(output_path, index=False)
    print(f"[INFO] Data berhasil disimpan ke {output_path}")

if __name__ == "__main__":
    main()

