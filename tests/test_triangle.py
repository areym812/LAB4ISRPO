import unittest
from itertools import permutations

from geometry import triangle


class TriangleTestCase(unittest.TestCase):
    def test_right_triangle_area(self):
        self.assertEqual(triangle.area(3, 4, 5), 6)

    def test_right_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_equilateral(self):
        self.assertAlmostEqual(triangle.area(2, 2, 2), 1.7320508075688772)
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_isosceles(self):
        self.assertEqual(triangle.area(5, 5, 6), 12)
        self.assertEqual(triangle.perimeter(5, 5, 6), 16)

    def test_fractional_sides(self):
        self.assertAlmostEqual(triangle.area(1.5, 2, 2.5), 1.5)
        self.assertAlmostEqual(triangle.perimeter(1.5, 2, 2.5), 6)

    def test_side_order(self):
        for sides in permutations((3, 4, 5)):
            with self.subTest(sides=sides):
                self.assertEqual(triangle.area(*sides), 6)
                self.assertEqual(triangle.perimeter(*sides), 12)

    def test_maximum_side(self):
        self.assertAlmostEqual(triangle.area(600_000_000, 800_000_000, 1_000_000_000), 2.4e17, delta=256)
        self.assertEqual(triangle.perimeter(600_000_000, 800_000_000, 1_000_000_000), 2_400_000_000)

    def test_degenerate_triangle(self):
        for function in (triangle.area, triangle.perimeter):
            for sides in permutations((1, 2, 3)):
                with self.subTest(function=function.__name__, sides=sides):
                    with self.assertRaises(ValueError):
                        function(*sides)

    def test_impossible_triangle(self):
        for function in (triangle.area, triangle.perimeter):
            for sides in permutations((1, 2, 4)):
                with self.subTest(function=function.__name__, sides=sides):
                    with self.assertRaises(ValueError):
                        function(*sides)

    def test_invalid_values_in_each_position(self):
        for function in (triangle.area, triangle.perimeter):
            for value in (0, -1, 1_000_000_001, float("nan"), float("inf")):
                for position in range(3):
                    sides = [3, 4, 5]
                    sides[position] = value
                    with self.subTest(function=function.__name__, sides=sides):
                        with self.assertRaises(ValueError):
                            function(*sides)

    def test_invalid_types_in_each_position(self):
        for function in (triangle.area, triangle.perimeter):
            for value in ("3", None, True, [3]):
                for position in range(3):
                    sides = [3, 4, 5]
                    sides[position] = value
                    with self.subTest(function=function.__name__, sides=sides):
                        with self.assertRaises(TypeError):
                            function(*sides)

