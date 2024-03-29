import unittest
import pytest
from nfceget import app
from nfceget.StateInvalidError import StateInvalidError

class test_app(unittest.TestCase):
    def test_qrcode_ok(self):
        data1 = app.json_from_file('./tests/html/pr/notaparana1.html')
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
    def test_qrcode_ok_2(self):
        data2 = app.json_from_file('./tests/html/pr/notaparana2.html')
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
    def test_qrcode_ok_3(self):
        data = app.json_from_file('./tests/html/pr/notaparana3.html')
        self.assertEqual(data['local']['name'], 'CONDOR SUPER CENTER LTDA')
        self.assertEqual(str(len(data['itens'])), data['totals']['quantityItens'])
        self.assertEqual(data['totals']['total'], '340,79')
        self.assertEqual(data['totals']['discounts'], '13,12')
        self.assertEqual(data['totals']['taxes'], '14,55')
        self.assertEqual(data['totals']['valueToPay'], '327,67')
        self.assertEqual(data['nfce']['chave'], '41200576189406004970651110001914871092220261')
        self.assertEqual(data['nfce']['numero'], '192287')
        self.assertEqual(data['nfce']['serie'], '111')
        self.assertEqual(data['nfce']['date'], '09/05/2020 14:20:26')
        self.assertEqual(data['nfce']['version'], '4.00')
        self.assertEqual(data['nfce']['protocolo'], '141202552953556')
        itemSample = data['itens'][0]
        self.assertEqual(itemSample['name'], 'REFRIG.ANTARC.GUAR.ZERO 2L PET')
        self.assertEqual(itemSample['quantity'], '1')
        self.assertEqual(itemSample['unit'], 'UN')
        self.assertEqual(itemSample['unitaryValue'], '4,99')
        self.assertEqual(itemSample['totalValue'], '4,99')
        self.assertEqual(itemSample['code'], '1283250')
        itemSample = data['itens'][9]
        self.assertEqual(itemSample['name'], 'SARDINHA GOMES COSTA OLEO 125G')
        self.assertEqual(itemSample['quantity'], '3')
        self.assertEqual(itemSample['unit'], 'UN')
        self.assertEqual(itemSample['unitaryValue'], '2,95')
        self.assertEqual(itemSample['totalValue'], '8,85')
        self.assertEqual(itemSample['code'], '3412480')
    def test_restadual_1(self):
        data = app.json_from_file('./tests/html/pr/receitaestadual1.html')
        print(data)
    def test_restadual_2(self):
        data = app.json_from_file('./tests/html/pr/receitaestadual2.html')
