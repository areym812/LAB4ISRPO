import unittest

from geometry import square


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_zero_area(self):
        self.assertEqual(square.area(0), 0)

    def test_zero_perimeter(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_unit_side(self):
        self.assertEqual(square.area(1), 1)
        self.assertEqual(square.perimeter(1), 4)

    def test_fractional_area(self):
        self.assertAlmostEqual(square.area(0.1), 0.01)

    def test_fractional_perimeter(self):
        self.assertAlmostEqual(square.perimeter(0.1), 0.4)

    def test_maximum_size(self):
        self.assertEqual(square.area(1_000_000_000), 10**18)
        self.assertEqual(square.perimeter(1_000_000_000), 4_000_000_000)

    def test_invalid_values(self):
        for function in (square.area, square.perimeter):
            for value in (-1, 1_000_000_001, float("nan"), float("inf")):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_invalid_types(self):
        for function in (square.area, square.perimeter):
            for value in ("5", None, True, [5]):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

