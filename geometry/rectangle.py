"""Площадь и периметр прямоугольника."""

from geometry.validation import check_size


def area(a, b):
    check_size(a)
    check_size(b)
    return a * b


def perimeter(a, b):
    check_size(a)
    check_size(b)
    return 2 * (a + b)

