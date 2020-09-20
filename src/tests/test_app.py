import unittest
from index import json_from_qrcode_link

class test_app(unittest.TestCase):
    def test_ok(self):
        data = json_from_qrcode_link('http://www.fazenda.pr.gov.br/nfce/qrcode?p=41200976430438005300650150002022071015187452|2|1|1|E9C67EF7E8B75CD401B3F6D3B1FD716ED22B3890')
        print(data)
        self.assertEqual(1, 1)