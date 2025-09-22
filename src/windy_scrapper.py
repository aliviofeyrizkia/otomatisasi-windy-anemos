import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_windy_screenshot(url, output="windy.png"):
    # Set Chrome Options untuk headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Buka Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    # Buka halaman windy
    driver.get(url)
    time.sleep(5)  # tunggu loading map

    # Simpan screenshot
    driver.save_screenshot(output)
    driver.quit()
    print(f"✅ Screenshot saved as {output}")
