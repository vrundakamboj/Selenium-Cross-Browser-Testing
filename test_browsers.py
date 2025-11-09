from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

# Create folder for screenshots (if not already present)
os.makedirs("screenshots", exist_ok=True)

# Browsers to test
browsers = ["chrome", "firefox", "safari"]  # Removed "edge"

for browser in browsers:
    print(f"\n🚀 Launching {browser}...")

    driver = None  # Initialize driver to None

    try:
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "safari":
            driver = webdriver.Safari()  # SafariDriver is built-in on macOS
        else:
            print(f"⚠️ Browser {browser} not supported yet.")
            continue

        # Open a test website
        driver.get("https://www.example.com")
        print(f"✅ {browser} loaded successfully → Title: {driver.title}")

        # Wait for 2 seconds
        time.sleep(2)

        # Take and save a screenshot
        screenshot_path = f"screenshots/{browser}_example.png"
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved at: {screenshot_path}")

    except Exception as e:
        print(f"❌ Error while testing {browser}: {e}")

    finally:
        # Close the browser if it was opened
        if driver:
            driver.quit()
            print(f"❎ {browser} closed successfully\n")
