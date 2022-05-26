import os
import shutil
import stat
import time

import git


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def create_test_repo():
    test_repo = os.path.join("test_data", "working")
    if os.path.isdir(test_repo):
        shutil.rmtree(test_repo, onerror=remove_readonly)
    working = git.Repo.init(test_repo)
    file = open(os.path.join("test_data", "working", "README.md"), 'x')
    ns = time.time_ns()
    file.write(str(ns))
    file.close()
    ul = working.untracked_files
    working.index.add(ul)
    working.index.commit("initial commit")





