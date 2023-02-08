import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def test_2_as_2(self):
        calc = Calculadora()
        self.assertEqual(5, calc.sumar(2, 2))


if __name__ == '__main__':
    unittest.main()
