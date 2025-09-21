from windy_scraper import capture_windy_screenshot

def main():
    url = "https://www.windy.com/-6.891/107.610"  # contoh lokasi: Dago Bandung
    image_path = capture_windy_screenshot(url, save_path="windy.png")
    print(f"[INFO] Screenshot tersimpan di: {image_path}")

if __name__ == "__main__":
    main()
