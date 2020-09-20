import unittest
import pytest
from index import json_from_qrcode_link, json_from_file
from lib.CustomEx import StateInvalidException
class test_app(unittest.TestCase):
    def test_url_invalid(self):
        with pytest.raises(StateInvalidException):
            json_from_qrcode_link('google.com')
    def test_url_empty(self):
        with pytest.raises(Exception):
            json_from_qrcode_link('')
    def test_url_none(self):
        with pytest.raises(Exception):
            json_from_qrcode_link(None)
    def test_ok(self):
        data = json_from_file('./nfce1.html')
        self.assertEqual(data.local.name, 'IRMAOS MUFFATO E CIA LTDA')