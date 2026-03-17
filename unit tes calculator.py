import unittest
from calculator import tambah, kurang, kali, bagi


class TestCalculator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah(5, 3), 8)

    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)

    def test_kali(self):
        self.assertEqual(kali(5, 3), 15)

    def test_bagi(self):
        self.assertEqual(bagi(6, 3), 2)


if __name__ == "__main__":
    unittest.main()