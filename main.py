from windy_scraper import capture_windy_screenshot

def main():
    url = "https://www.windy.com/-6.935/107.606/gfs?gfs,rh,-7.331,107.606,9,m:dtBai8v"  # contoh lokasi: Dago Bandung
    image_path = capture_windy_screenshot(url, save_path="windy.png")
    print(f"[INFO] Screenshot tersimpan di: {image_path}")

if __name__ == "__main__":
    main()
