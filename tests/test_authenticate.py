from command.cas import Cas


def test_authenticate_text_file():
    cas = Cas()
    res = cas.authenticate("tests/data/Aneudy_Resume.txt")
    assert res.get("Status") == "TRUSTED"


#def test_authenticate_git_repo():
#    cas = Cas()
#    res = cas.authenticate("path/to/git/repo")
#    assert res.get("Status") == "TRUSTED"
