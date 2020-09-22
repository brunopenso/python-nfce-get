import unittest
import pytest
from nfceget import Nfceget

class test_class(unittest.TestCase):
    def test1(self):
        json = Nfceget.from_file('./tests/html/nfce1.html')
        self.assertEqual(len(json['itens']), 26)