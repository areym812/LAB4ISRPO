"""Общие правила проверки размеров фигур."""

import math

MAX_SIZE = 1_000_000_000


def check_size(value):
    """Разрешены int и float от 0 до MAX_SIZE; bool не является размером."""
    if type(value) not in (int, float):
        raise TypeError("Размер должен быть числом int или float")
    if value < 0 or value > MAX_SIZE or not math.isfinite(value):
        raise ValueError("Размер должен быть конечным числом от 0 до 1000000000")

