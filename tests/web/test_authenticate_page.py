import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.authenticate_page import AuthenticatePage
from base.ui_driver import UIDriver


class TestAuthenticatePage:

    def test_authenticate_page(self):
        browser = UIDriver().get_driver()
        auth_page = AuthenticatePage(driver=browser)
        auth_page.navigate()
        signer_id = "aneudy.motacatalino@gmail.com"
        unique_hash = "704d5e623f1942679e956b06fc7c1379f43b2eedaba096669337069fe0b3daae"
        auth_page.type_signer_id(signer_id)
        auth_page.fill_asset_hash(unique_hash)
        auth_page.click_green_button()
        # assert auth_page.get_signer_id() == signer_id
        # assert auth_page.get_unique_hash() == unique_hash
        assert auth_page.get_asset_status() == "Trusted"
