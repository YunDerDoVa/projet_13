import tempfile
from django.test import TestCase
from django.conf import settings

from virustotal.analyzer import Analyzer


class AnalyserTestCase(TestCase):

    def setUp(self) -> None:
        self.file = tempfile.NamedTemporaryFile()
        self.file.name = 'inoffensive_file.txt'
        self.mode = 'w'

    def test_scan_file(self):

        analyzer = Analyzer(settings.TOTALVIRUS_API_KEY)
        json = analyzer.scan_file(self.file)

        self.assertEqual(json.status_code, 200)
