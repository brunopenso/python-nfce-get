import unittest
import pytest
from index import json_from_qrcode_link, json_from_file
from module.Errors import StateInvalidException

class test_app(unittest.TestCase):
    def test_url_invalid(self):
        with pytest.raises(StateInvalidException):
            json_from_qrcode_link('google.com')
    def test_url_empty(self):
        with pytest.raises(ValueError):
            json_from_qrcode_link('')
    def test_url_none(self):
        with pytest.raises(ValueError):
            json_from_qrcode_link(None)
    def test_ok(self):
        data = json_from_file('./tests/html/nfce1.html')
        self.assertEqual(data['local']['name'], 'IRMAOS MUFFATO E CIA LTDA')
        self.assertEqual(len(data['itens']), 26)
        self.assertEqual(len(data['itens']), 26)
        itemProvolone = data['itens'][1]
        self.assertEqual(itemProvolone['name'], 'QUEIJO PROVOLONE KG')
        self.assertEqual(itemProvolone['quantity'], '0,266')
        self.assertEqual(itemProvolone['unit'], 'Kg')
        self.assertEqual(itemProvolone['unitaryValue'], '63,99')
        self.assertEqual(itemProvolone['totalValue'], '17,02')
