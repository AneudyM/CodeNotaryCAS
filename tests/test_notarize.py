from command.cas import Cas


def test_notarize_text_file():
    cas = Cas()
    res = cas.notarize("test_data/Aneudy_Resume.txt")
    assert res.get("Status") == "TRUSTED"


def test_notarize_git_repo():
    # Arrange
    cas = Cas()
    #repo_name = utils.generate_repo()

    # Act
    res = cas.notarize_repo("test_data/my-repo-01")

    # Assert
    assert res.get("Status") == "TRUSTED"
