import unittest
import pytest
from nfceget import app
from nfceget.StateInvalidError import StateInvalidError

class test_app(unittest.TestCase):
    def test_url_invalid(self):
        with pytest.raises(Exception):
            app.json_from_qrcode_link('google.com')
    def test_url_empty(self):
        with pytest.raises(ValueError):
            app.json_from_qrcode_link('')
    def test_url_none(self):
        with pytest.raises(ValueError):
            app.json_from_qrcode_link(None)
