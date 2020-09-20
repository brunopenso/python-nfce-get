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
        data1 = json_from_file('./tests/html/nfce1.html')
        self.assertEqual(data1['local']['name'], 'IRMAOS MUFFATO E CIA LTDA')
        self.assertEqual(len(data1['itens']), 26)
        itemProvolone = data1['itens'][1]
        self.assertEqual(itemProvolone['name'], 'QUEIJO PROVOLONE KG')
        self.assertEqual(itemProvolone['quantity'], '0,266')
        self.assertEqual(itemProvolone['unit'], 'Kg')
        self.assertEqual(itemProvolone['unitaryValue'], '63,99')
        self.assertEqual(itemProvolone['totalValue'], '17,02')
    def test_ok_2(self):
        data2 = json_from_file('./tests/html/nfce2.html')
        self.assertEqual(data2['local']['name'], 'CONDOR SUPER CENTER LTDA')
        self.assertEqual(len(data2['itens']), 56)
        self.assertEqual(data2['totals']['quantityItens'], '56')
        self.assertEqual(data2['totals']['total'], '361,51')
        self.assertEqual(data2['totals']['discounts'], '17,00')
        self.assertEqual(data2['totals']['taxes'], '12,23')
        self.assertEqual(data2['totals']['valueToPay'], '344,51')
