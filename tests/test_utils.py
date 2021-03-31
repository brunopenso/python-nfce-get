import unittest
from nfceget.util import clear_text, normalize_key, remove_numbers

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
    def test_remove_number(self):
        value = remove_numbers('abc') 
        self.assertEqual(value, 'abc')
        value = remove_numbers('abc123') 
        self.assertEqual(value, 'abc')
        value = remove_numbers('123') 
        self.assertEqual(value, '')
        value = remove_numbers('42a3') 
        self.assertEqual(value, 'a')