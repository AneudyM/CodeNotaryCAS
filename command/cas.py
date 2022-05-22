import subprocess
import utils.parser


class Cas:

    CAS_API_KEY = ""

    def notarize(self, asset):
        cp = subprocess.run(['cas', 'notarize', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse(cp.stdout)

    def authenticate(self, asset):
        cp = subprocess.run(['cas', 'authenticate', asset, '--api-key', self.CAS_API_KEY],
                            capture_output=True, universal_newlines=True)
        return utils.parser.parse(cp.stdout)
