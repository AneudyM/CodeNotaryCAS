import os
import subprocess
import utils.parser


class Cas:

    CAS_API_KEY = os.environ.get("CAS_API_KEY")

    def notarize(self, asset):
        cp = subprocess.run(['cas', 'notarize', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_stdout(cp.stdout)

    def notarize_repo(self, repo_path):
        cp = subprocess.run(['cas', 'notarize', 'git://' + repo_path, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_stdout(cp.stdout)

    def authenticate(self, asset):
        cp = subprocess.run(['cas', 'authenticate', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_stdout(cp.stdout)
