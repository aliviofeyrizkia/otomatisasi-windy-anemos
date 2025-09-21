from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def img_scraper(url, filename="windy.png"):
    # Setup headless browser (tanpa tampilan GUI)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Tunggu beberapa detik agar peta & layer Windy termuat
    time.sleep(10)

    # Screenshot halaman
    driver.save_screenshot(filename)
    driver.quit()
    print(f"Screenshot tersimpan: {filename}")
