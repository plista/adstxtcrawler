import unittest
from httmock import urlmatch, HTTMock
from app.app import App
import os


@urlmatch(netloc=r'(.*\.)?spiegel\.de')
def google_mock(url, request):
    path = "%s/fixtures/%s.txt" % (os.path.dirname(os.path.realpath(__file__)), url.netloc)
    with open(path) as f:
        return f.read()


class TestPlista(unittest.TestCase):

    def test_apn_standard(self):
        url = "spiegel.de"

        # open context to patch
        with HTTMock(google_mock):
            app = App(["appnexus.com, 3563, DIRECT"])
            app.queue(url)
            result = app.run("/tmp/foo.csv")
            self.assertEqual({'matches': 1, 'misses': 0}, result)
