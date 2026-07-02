import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# NOTE: This script assumes a logged-in DeepSeek browser session and a visible chat input box.


def send_deepseek_message(message: str, headless: bool = False) -> bool:
    options = Options()
    if headless:
        options.headless = True
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=ChromeService(), options=options)
    try:
        driver.get('https://chat.deepseek.com/')
        time.sleep(3)

        # Wait for the DeepSeek input textarea to appear
        textarea = None
        for _ in range(10):
            try:
                textarea = driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Message DeepSeek"]')
                if textarea:
                    break
            except Exception:
                time.sleep(1)

        if textarea is None:
            print('DeepSeek input box not found.')
            return False

        textarea.click()
        textarea.clear()
        textarea.send_keys(message)
        textarea.send_keys(Keys.ENTER)

        time.sleep(2)
        return True
    finally:
        driver.quit()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Send a message to DeepSeek chat.')
    parser.add_argument('message', help='The message to send to DeepSeek.')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode.')
    args = parser.parse_args()

    success = send_deepseek_message(args.message, headless=args.headless)
    print('Message sent' if success else 'Failed to send message')
