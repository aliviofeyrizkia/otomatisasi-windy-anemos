from src.windy_scraper import capture_windy_screenshot

if __name__ == "__main__":
    capture_windy_screenshot(
        url="https://www.windy.com/-6.935/107.606",
        output="windy.png"
    )
