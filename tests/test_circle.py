import unittest

from geometry import circle


class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(3), 28.274333882308138)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.84955592153876)

    def test_zero_area(self):
        self.assertEqual(circle.area(0), 0)

    def test_zero_perimeter(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), 3.141592653589793)
        self.assertAlmostEqual(circle.perimeter(1), 6.283185307179586)

    def test_fractional_area(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)

    def test_fractional_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793)

    def test_maximum_size(self):
        self.assertAlmostEqual(circle.area(1_000_000_000), 3.141592653589793e18, delta=4000)
        self.assertAlmostEqual(circle.perimeter(1_000_000_000), 6.283185307179586e9, delta=0.00001)

    def test_invalid_values(self):
        for function in (circle.area, circle.perimeter):
            for value in (-1, 1_000_000_001, float("nan"), float("inf")):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_invalid_types(self):
        for function in (circle.area, circle.perimeter):
            for value in ("3", None, True, [3]):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

