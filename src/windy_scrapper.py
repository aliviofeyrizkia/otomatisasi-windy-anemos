from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def capture_windy_screenshot(url, save_path="windy.png", wait_time=5):
    """
    Ambil screenshot dari halaman Windy menggunakan Selenium.
    Args:
        url (str): URL Windy
        save_path (str): path untuk menyimpan screenshot
        wait_time (int): waktu tunggu (detik) agar halaman ter-load
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)

    time.sleep(wait_time)  # tunggu halaman load

    driver.save_screenshot(save_path)
    driver.quit()
    return save_path

