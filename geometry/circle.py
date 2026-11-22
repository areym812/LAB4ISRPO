"""Площадь круга и длина окружности."""

import math

from geometry.validation import check_size


def area(r):
    check_size(r)
    return math.pi * r * r


def perimeter(r):
    check_size(r)
    return 2 * math.pi * r

