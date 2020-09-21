import unittest
from nfceget.util import clear_text, normalize_key

class test_utils(unittest.TestCase):
    def test_normalizekey_empty(self):
        value = normalize_key('')
        self.assertEqual(value, '')
    def test_normalizekey_none(self):
        value = normalize_key(None)
        self.assertEqual(value, '')
    def test_normalizekey_nfce(self):
        value = normalize_key('3333 3333 2232 a b c')
        self.assertEqual(value, '333333332232abc')
    def test_cleartext_empty(self):
        value = clear_text('')
        self.assertEqual(value, '')
    def test_cleartext_none(self):
        value = clear_text(None)
        self.assertEqual(value, '')