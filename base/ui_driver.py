from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class UIDriver:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    def get_driver(self):
        return self.driver
