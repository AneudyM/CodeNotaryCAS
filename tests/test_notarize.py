import os
import subprocess

from command.cas import Cas


def test_notarize_file():
    cas = Cas()
    cas.login()
    res = cas.notarize_file("Aneudy_Resume.txt")
    print(res)
    print(res.get("Kind"))


def test_notarize_git_repo():
    cas = Cas()
    cas.login()
#   res = cas.notarize_repo()
#     assert res.get('verified') is True
#
#
# def test_notarize_docker_image():
#     cas = Cas()
#     res = cas.notarize_docker_image("cas-automation")
#     assert res.get('verified') is True
