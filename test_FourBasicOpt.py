import unittest
from FourBasicOpt import FourBasicOpt

class FourBasicOptTest(unittest.TestCase):
    def test_add_01(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.add(100, 10), 110)

    def test_add_02(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.add(100, -10), 90)

    def test_sub_01(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.subtract(100, 10), 90)

    def test_sub_02(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.subtract(100, -10), 110)

    def test_div_01(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.divide(100, 10), 10)

    def test_div_02(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.divide(100, -10), -10)

    def test_mul_01(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.multiply(100, 10), 1000)

    def test_mul_02(self):
        four_opt = FourBasicOpt()
        self.assertEqual(four_opt.multiply(100, -10), -1000)

if __name__ == '__main__':
    unittest.main()