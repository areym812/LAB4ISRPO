"""Площадь по формуле Герона и периметр треугольника."""

import math

from geometry.validation import check_size


def check_triangle(a, b, c):
    for side in (a, b, c):
        check_size(side)
    if a == 0 or b == 0 or c == 0:
        raise ValueError("Стороны треугольника должны быть положительными")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Сумма двух сторон должна быть больше третьей")


def area(a, b, c):
    check_triangle(a, b, c)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    check_triangle(a, b, c)
    return a + b + c

