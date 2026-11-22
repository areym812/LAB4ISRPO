import unittest

from geometry import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

    def test_zero_first_side(self):
        self.assertEqual(rectangle.area(0, 10), 0)
        self.assertEqual(rectangle.perimeter(0, 10), 20)

    def test_zero_second_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.perimeter(10, 0), 20)

    def test_both_zero(self):
        self.assertEqual(rectangle.area(0, 0), 0)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_square(self):
        self.assertEqual(rectangle.area(10, 10), 100)
        self.assertEqual(rectangle.perimeter(10, 10), 40)

    def test_fractional_sides(self):
        self.assertAlmostEqual(rectangle.area(0.1, 0.2), 0.02)
        self.assertAlmostEqual(rectangle.perimeter(0.1, 0.2), 0.6)

    def test_side_order(self):
        self.assertEqual(rectangle.area(4, 3), 12)
        self.assertEqual(rectangle.perimeter(4, 3), 14)

    def test_maximum_size(self):
        self.assertEqual(rectangle.area(1_000_000_000, 1_000_000_000), 10**18)
        self.assertEqual(rectangle.perimeter(1_000_000_000, 1_000_000_000), 4_000_000_000)

    def test_invalid_values_in_each_position(self):
        for function in (rectangle.area, rectangle.perimeter):
            for value in (-1, 1_000_000_001, float("nan"), float("inf")):
                for sides in ((value, 4), (3, value)):
                    with self.subTest(function=function.__name__, sides=sides):
                        with self.assertRaises(ValueError):
                            function(*sides)

    def test_invalid_types_in_each_position(self):
        for function in (rectangle.area, rectangle.perimeter):
            for value in ("3", None, True, [3]):
                for sides in ((value, 4), (3, value)):
                    with self.subTest(function=function.__name__, sides=sides):
                        with self.assertRaises(TypeError):
                            function(*sides)

