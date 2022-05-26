import os
import pytest
import utils.repo
import time

from command.cas import Cas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.mark.order(1)
def test_notarize_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'ANEUDY_MOTA.txt')
    print(test_file)
    print(os.getcwd())
    file = open(test_file, 'x')
    ns = time.time_ns()
    file.write(str(ns))
    file.close()
    cas = Cas()
    cas.login()
    res = cas.notarize_file(test_file)
    assert res.get('Status') == "TRUSTED"


@pytest.mark.order(2)
def test_authenticate_notarized_file():
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
def test_authenticate_notarized_git_repo():
    test_repo = os.path.join(os.getcwd(), 'test_data', 'working')
    cas = Cas()
    cas.login()
    res = cas.authenticate_repo(test_repo)
    assert res.get('verified') is True


def test_authenticate_non_notarized_asset():
    unknown_asset = os.path.join(os.getcwd(), 'test_data', 'non_notarized_file.txt')
    file = open(unknown_asset, 'x')
    ns = time.time_ns()
    file.write(str(ns))
    file.close()
    cas = Cas()
    cas.login()
    res = cas.authenticate_file(unknown_asset)
    assert 'was not notarized' in res


@pytest.mark.order(5)
def test_authenticate_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    test_file = os.path.join(os.getcwd(), 'test_data', 'ANEUDY_MOTA.txt')
    cas = Cas()
    cas.login()
    res = cas.authenticate_file(test_file)
    print(res.__getitem__('signer'))
    signer_id = res.__getitem__('signer')
    asset_hash = res.__getitem__('hash')
    driver.get("https://cas.codenotary.com/authenticate/" + signer_id + "/" + asset_hash)
    assert driver.title == "cas - cas attestation service"
    driver.quit()

