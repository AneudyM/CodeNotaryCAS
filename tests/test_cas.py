import os
import pytest
import utils.repo

from command.cas import Cas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.mark.order(1)
def test_notarize_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'ANEUDY_MOTA.txt')
    cas = Cas()
    cas.login()
    res = cas.notarize_file(test_file)
    assert res.get('Status') == "TRUSTED"

@pytest.mark.order(2)
def test_authenticate_text_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'ANEUDY_MOTA.txt')
    cas = Cas()
    cas.login()
    res = cas.authenticate_file(test_file)
    assert res.get('verified') is True


@pytest.mark.order(3)
def test_notarize_git_repo():
    test_repo = os.path.join(os.getcwd(), 'test_data', 'working')
    cas = Cas()
    cas.login()
    utils.repo.create_test_repo()
    res = cas.notarize_repo(test_repo)
    assert res.get('verified') is True


@pytest.mark.order(4)
def test_authenticate_git_repo():
    test_repo = os.path.join(os.getcwd(), 'test_data', 'working')
    cas = Cas()
    cas.login()
    res = cas.authenticate_repo(test_repo)
    assert res.get('verified') is True


@pytest.mark.order(5)
def test_authenticate_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("https://cas.codenotary.com/authenticate")
    assert driver.title == "cas - cas attestation service"
    driver.quit()

