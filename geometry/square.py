"""Площадь и периметр квадрата."""

from geometry.validation import check_size


def area(a):
    check_size(a)
    return a * a


def perimeter(a):
    check_size(a)
    return 4 * a

