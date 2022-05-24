import os

import utils.repo
from command.cas import Cas


def test_notarize_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'Aneudy_Resume.txt')
    cas = Cas()
    cas.login()
    res = cas.notarize_file(test_file)
    assert res.get('Status') == "TRUSTED"


def test_notarize_git_repo():
    test_repo = os.path.join(os.getcwd(), 'test_data', 'working')
    cas = Cas()
    cas.login()
    utils.repo.create_test_repo()
    res = cas.notarize_repo(test_repo)
    assert res.get('verified') is True
