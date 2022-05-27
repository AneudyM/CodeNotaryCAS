import os
import pytest
import utils.repo
import time

from command.cas import Cas


@pytest.mark.order(1)
def test_notarize_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'ANEUDY_MOTA.txt')
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

