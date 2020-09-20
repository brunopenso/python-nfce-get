import unittest
import pytest
from index import json_from_qrcode_link, json_from_file
from module.Errors import StateInvalidException
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
