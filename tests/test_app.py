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
    def test_ok(self):
        data1 = app.json_from_file('./tests/html/nfce1.html')
        self.assertEqual(data1['local']['name'], 'IRMAOS MUFFATO E CIA LTDA')
        self.assertEqual(len(data1['itens']), 26)
        itemSample = data1['itens'][1]
        self.assertEqual(itemSample['name'], 'QUEIJO PROVOLONE KG')
        self.assertEqual(itemSample['quantity'], '0,266')
        self.assertEqual(itemSample['unit'], 'Kg')
        self.assertEqual(itemSample['unitaryValue'], '63,99')
        self.assertEqual(itemSample['totalValue'], '17,02')
        self.assertEqual(data1['nfce']['chave'], '41200976430488885300650150002022071015187452')
        self.assertEqual(data1['nfce']['numero'], '332207')
        self.assertEqual(data1['nfce']['serie'], '15')
        self.assertEqual(data1['nfce']['date'], '01/09/2020 15:22:18')
        self.assertEqual(data1['nfce']['version'], '4.00')
        self.assertEqual(data1['nfce']['protocolo'], '141201339877471')
    def test_ok_2(self):
        data2 = app.json_from_file('./tests/html/nfce2.html')
        self.assertEqual(data2['local']['name'], 'CONDOR SUPER CENTER LTDA')
        self.assertEqual(len(data2['itens']), 56)
        self.assertEqual(data2['totals']['quantityItens'], '56')
        self.assertEqual(data2['totals']['total'], '361,51')
        self.assertEqual(data2['totals']['discounts'], '17,00')
        self.assertEqual(data2['totals']['taxes'], '12,23')
        self.assertEqual(data2['totals']['valueToPay'], '344,51')
        self.assertEqual(data2['nfce']['chave'], '41200976555506004970651070001694781121134117')
        self.assertEqual(data2['nfce']['numero'], '167878')
        self.assertEqual(data2['nfce']['serie'], '107')
        self.assertEqual(data2['nfce']['date'], '12/09/2020 11:34:12')
        self.assertEqual(data2['nfce']['version'], '4.00')
        self.assertEqual(data2['nfce']['protocolo'], '141245057599014')
        itemSample = data2['itens'][55]
        self.assertEqual(itemSample['name'], 'BOMBOM LACTA FAVORITOS 250,6G')
        self.assertEqual(itemSample['quantity'], '1')
        self.assertEqual(itemSample['unit'], 'UN')
        self.assertEqual(itemSample['unitaryValue'], '9,49')
        self.assertEqual(itemSample['totalValue'], '9,49')
        self.assertEqual(itemSample['code'], '15213680')
