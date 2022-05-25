import os.path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_authenticate_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("https://cas.codenotary.com/authenticate")
    assert driver.title == "cas - cas attestation service"
    driver.quit()
