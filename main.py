"""Консольная программа для ручных проверок."""

import argparse

from geometry import circle, rectangle, square, triangle


def main():
    parser = argparse.ArgumentParser(description="Площадь и периметр фигур")
    parser.add_argument("figure", choices=["rectangle", "square", "circle", "triangle"])
    parser.add_argument("sizes", nargs="+", type=float, help="Размеры фигуры через пробел")
    args = parser.parse_args()
    figures = {
        "rectangle": (rectangle, 2),
        "square": (square, 1),
        "circle": (circle, 1),
        "triangle": (triangle, 3),
    }
    module, count = figures[args.figure]
    if len(args.sizes) != count:
        parser.error(f"Для {args.figure} требуется размеров: {count}")
    try:
        s = module.area(*args.sizes)
        p = module.perimeter(*args.sizes)
    except (TypeError, ValueError) as error:
        parser.error(str(error))
    print(f"Площадь: {s:.10g}")
    print(f"Периметр: {p:.10g}")


if __name__ == "__main__":
    main()

