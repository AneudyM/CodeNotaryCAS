import os
import subprocess
import sys

import utils.parser


class Cas:
    CAS_API_KEY = os.getenv('CAS_API_KEY')
    CAS_BIN = os.path.join(os.getcwd(), 'bin', 'cas')
    TEST_DATA_DIR = os.path.join(os.getcwd(), 'test_data')

    def login(self):
        cp = subprocess.run([self.CAS_BIN, 'login'], capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)

    def logout(self):
        cp = subprocess.run([self.CAS_BIN, 'logout'], capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)

    def notarize_file(self, asset):
        cp = subprocess.run(
            [self.CAS_BIN, 'notarize', os.path.join(self.TEST_DATA_DIR, asset), '--api-key', self.CAS_API_KEY],
            capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)
        return utils.parser.parse_stdout(cp.stdout)

    def notarize_repo(self, repo_path):
        cp = subprocess.run(
            [self.CAS_BIN, 'notarize', 'git://' + repo_path, '--api-key', self.CAS_API_KEY, '--output=json'],
            capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)
        return utils.parser.parse_json(cp.stdout)

    def notarize_docker_image(self, image_name):
        cp = subprocess.run(
            [self.CAS_BIN, 'notarize', 'docker://' + image_name, '--api-key', self.CAS_API_KEY, '--output=json'],
            capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)
        return utils.parser.parse_json(cp.stdout)

    def authenticate_file(self, asset):
        cp = subprocess.run(
            [self.CAS_BIN, 'authenticate', asset, '--api-key', self.CAS_API_KEY, '--output=json'],
            capture_output=True, universal_newlines=True)
        if cp.stderr:
            return cp.stderr
        return utils.parser.parse_json(cp.stdout)

    def authenticate_repo(self, test_repo):
        cp = subprocess.run(
            [self.CAS_BIN, 'authenticate', 'git://' + test_repo, '--api-key', self.CAS_API_KEY, '--output=json'],
            capture_output=True, universal_newlines=True)
        if cp.stderr:
            sys.exit(cp.stderr)
        return utils.parser.parse_json(cp.stdout)

    def authenticate_docker_image(self):
        pass
