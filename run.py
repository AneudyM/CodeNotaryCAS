import os
import shutil
import stat
import subprocess
import sys
import time

import pytest

from git import Repo


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def clone_repo(repo_url, target_dir):
    Repo.clone_from(repo_url, target_dir)


def make_cas():
    subprocess.run(['make', 'cas'])


if __name__ == "__main__":
    project_base_dir = os.getcwd()
    bin_dir = os.path.join("bin")
    cas_repo_path = os.path.join("test_data", "cas")
    url = 'https://github.com/codenotary/cas.git'

    if "CAS_API_KEY" not in os.environ:
        sys.exit("CAS_API_KEY not set")

    if os.path.isdir(bin_dir):
        shutil.rmtree(bin_dir, onerror=remove_readonly)
        clone_repo(url, bin_dir)
        os.chdir(bin_dir)
        make_cas()
    else:
        clone_repo(url, bin_dir)
        os.chdir(bin_dir)
        make_cas()



    os.chdir(project_base_dir)
    sys.exit(pytest.main(['-s']))
