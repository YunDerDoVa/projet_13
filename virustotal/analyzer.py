import requests


class Analyzer:
    """ Analyzer is implemented with virustotal's api. It's executed
     when a javascript code is posted but any user to check
      if the file is secure. """

    def __init__(self, api_key):
        self.api_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        self.params = {'apikey': api_key}

    def scan_file(self, file):
        """ This method scan a file passed in parameter to check
        return a virustotal's rapport. """

        files = {'file': (file.filename, file.open('rb'))}

        response = requests.post(self.api_url, files=files, params=self.params)

        return response.json()
