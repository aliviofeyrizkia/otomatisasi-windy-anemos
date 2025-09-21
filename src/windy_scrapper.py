from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def capture_windy_screenshot(url, save_path="windy.png"):
    options = Options()
    options.add_argument("--headless")        # jalankan tanpa buka jendela GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(5)  # tunggu elemen Windy benar2 muncul

    driver.save_screenshot(save_path)
    driver.quit()
    return save_path
