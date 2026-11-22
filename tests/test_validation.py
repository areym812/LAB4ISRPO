import unittest

from geometry.validation import check_size


class ValidationTestCase(unittest.TestCase):
    def test_zero(self):
        self.assertIsNone(check_size(0))

    def test_positive_integer(self):
        self.assertIsNone(check_size(12))

    def test_positive_float(self):
        self.assertIsNone(check_size(0.25))

    def test_maximum_size(self):
        self.assertIsNone(check_size(1_000_000_000))

    def test_above_maximum(self):
        with self.assertRaises(ValueError):
            check_size(1_000_000_001)

    def test_negative(self):
        with self.assertRaises(ValueError):
            check_size(-0.001)

    def test_non_finite(self):
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    check_size(value)

    def test_wrong_types(self):
        for value in ("2", None, [], {}, 2j):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    check_size(value)

    def test_boolean(self):
        for value in (True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    check_size(value)

