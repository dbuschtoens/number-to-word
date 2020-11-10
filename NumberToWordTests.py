import unittest

from NumberToWord import NumberToWord

class NumberToWordTests(unittest.TestCase):

    def test_1(self):
        self.assertEqual("one", NumberToWord(1))


    def test_42(self):
        self.assertEqual("fourty two", NumberToWord(1))


    def test_1337(self):
        self.assertEqual("one thousand three hundred thirty seven", NumberToWord(1))

if __name__ == '__main__':
    unittest.main()
