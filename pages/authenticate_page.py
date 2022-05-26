from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthenticatePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://cas.codenotary.com/authenticate/"

    def navigate(self):
        self.driver.get(self.url)

    def type_signer_id(self, signer_id):
        signer_id_field = self.driver.find_element(
            By.XPATH,
            '//input[@placeholder="Signer ID (email)"]')
        signer_id_field.clear()
        signer_id_field.send_keys(signer_id)
        return None

    def fill_asset_hash(self, asset_hash):
        asset_hash_field = self.driver.find_element(
            By.XPATH,
            '//input[@type="text"]')
        asset_hash_field.clear()
        asset_hash_field.send_keys(asset_hash)
        return None

    def click_green_button(self):
        green_check_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="app"]/div/main/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/button')
        green_check_button.click()
        return None

    def get_asset_status(self):
        authenticate_chip_status = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.CLASS_NAME,
            'v-chip__content')),
            "Timed out waiting for element.")
        return authenticate_chip_status.text
