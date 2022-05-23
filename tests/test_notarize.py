from command.cas import Cas


def test_notarize_text_file():
    cas = Cas()
    res = cas.notarize_text_file("test_data/Aneudy_Resume.txt")
    assert res.get("Status") == "TRUSTED"


def test_notarize_git_repo():
    cas = Cas()
    res = cas.notarize_repo("test_data/my-repo-01")
    assert res.get('verified') is True


def test_notarize_docker_image():
    cas = Cas()
    res = cas.notarize_docker_image("cas-automation")
    assert res.get('verified') is True


