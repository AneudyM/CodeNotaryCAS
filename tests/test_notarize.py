from command.cas import Cas


def test_notarize_text_file():
    cas = Cas()
    res = cas.notarize("tests/data/Aneudy_Resume.txt")
    assert res.get("Status") == "TRUSTED"


#def test_notarize_git_repo():
#    cas = Cas()
#    res = cas.notarize("path/to/git/repo")
#    assert res.get("Status") == "TRUSTED"
