
import os

import pytest

from command.cas import Cas


@pytest.mark.order(2)
def test_authenticate_text_file():
    test_file = os.path.join(os.getcwd(), 'test_data', 'Aneudy_Resume.txt')
    cas = Cas()
    cas.login()
    res = cas.authenticate_file(test_file)
    assert res.get('verified') is True


@pytest.mark.order(4)
def test_authenticate_git_repo():
    test_repo = os.path.join(os.getcwd(), 'test_data', 'working')
    cas = Cas()
    cas.login()
    res = cas.authenticate_repo(test_repo)
    assert res.get('verified') is True
