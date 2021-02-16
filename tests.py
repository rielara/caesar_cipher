import unittest
from caesar_cipher import encrypted_message

class TestCaesar(unittest.TestCase):

    def test_cipher(self):
        encrypted = encrypted_message('salut', 1)
        self.assertEqual('tbmvu', encrypted)

    def test_symbol(self):
        encrypted = encrypted_message('he\'s', 1)
        self.assertEqual('if\'t', encrypted)


if __name__ == '__main__':
    unittest.main()