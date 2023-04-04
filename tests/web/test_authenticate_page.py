
from pages.authenticate_page import AuthenticatePage
from base.ui_driver import UIDriver


class TestAuthenticatePage:

    def test_authenticate_page(self):
        signer_id = "aneudy.motacatalino@gmail.com"
        unique_hash = "704d5e623f1942679e956b06fc7c1379f43b2eedaba096669337069fe0b3daae"
        browser = UIDriver().get_driver()
        auth_page = AuthenticatePage(driver=browser)
        auth_page.navigate()
        auth_page.type_signer_id(signer_id)
        auth_page.fill_asset_hash(unique_hash)
        auth_page.click_green_button()
        assert auth_page.get_asset_status() == "Trusted"

    # def test_authenticate_page_url(self):
    #     signer_id = b"aneudy.motacatalino@gmail.com"
    #     unique_hash = "704d5e623f1942679e956b06fc7c1379f43b2eedaba096669337069fe0b3daae"
    #     base64_encoded_signer_id = base64.b64encode(signer_id)
    #     browser = UIDriver().get_driver()
    #     auth_page = AuthenticatePage(driver=browser)
    #     auth_page.url = "https://cas.codenotary.com/authenticate/" + base64_encoded_signer_id.decode() + "/" + unique_hash
    #     auth_page.navigate()
    #     assert auth_page.get_asset_status() == "Trusted"


