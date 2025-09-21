import cv2
import pytesseract
import pandas as pd

def crop_and_ocr(image_path, crop_coords, column_name):
    """
    Crop bagian gambar sesuai koordinat dan lakukan OCR.
    Args:
        image_path (str): path gambar input
        crop_coords (tuple): koordinat crop (x1, y1, x2, y2)
        column_name (str): nama kolom untuk hasil OCR
    Returns:
        pd.DataFrame: DataFrame berisi hasil OCR
    """
    # Baca gambar
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError(f"Gambar tidak ditemukan: {image_path}")

    # Crop gambar
    x1, y1, x2, y2 = crop_coords
    cropped = img[y1:y2, x1:x2]

    # OCR dengan Tesseract
    text = pytesseract.image_to_string(cropped, config="--psm 6").strip()

    # Pecah ke dalam baris (misal tiap jam/dataset terpisah baris)
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Simpan ke DataFrame
    df = pd.DataFrame(lines, columns=[column_name])
    return df

