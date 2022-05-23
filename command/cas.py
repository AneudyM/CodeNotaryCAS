import os
import subprocess
import utils.parser


class Cas:

    CAS_API_KEY = os.environ.get("CAS_API_KEY")

    def notarize_text_file(self, asset):
        cp = subprocess.run(['cas', 'notarize', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_stdout(cp.stdout)

    def notarize_repo(self, repo_path):
        cp = subprocess.run(['cas', 'notarize', 'git://' + repo_path, '--api-key', self.CAS_API_KEY, '--output=json'],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_json(cp.stdout)

    def notarize_docker_image(self, image_name):
        cp = subprocess.run(['cas', 'notarize', 'docker://' + image_name, '--api-key', self.CAS_API_KEY, '--output=json'],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_json(cp.stdout)

    def authenticate(self, asset):
        cp = subprocess.run(['cas', 'authenticate', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse_stdout(cp.stdout)
