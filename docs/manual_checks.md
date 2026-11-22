# Протокол консольных проверок

Проверки выполнены запуском программы; ожидания заданы заранее. Это функциональные проверки CLI, отдельно от 51 unit-теста.

## M01 — python3 main.py rectangle 3 4

Ожидание: Площадь: 12; Периметр: 14. Код завершения: 0.

```text
Площадь: 12
Периметр: 14
```

Результат: пройдено.

## M02 — python3 main.py rectangle 10 0

Ожидание: Площадь: 0; Периметр: 20. Код завершения: 0.

```text
Площадь: 0
Периметр: 20
```

Результат: пройдено.

## M03 — python3 main.py rectangle 0.1 0.2

Ожидание: Площадь: 0.02; Периметр: 0.6. Код завершения: 0.

```text
Площадь: 0.02
Периметр: 0.6
```

Результат: пройдено.

## M04 — python3 main.py square 5

Ожидание: Площадь: 25; Периметр: 20. Код завершения: 0.

```text
Площадь: 25
Периметр: 20
```

Результат: пройдено.

## M05 — python3 main.py square 0

Ожидание: Площадь: 0; Периметр: 0. Код завершения: 0.

```text
Площадь: 0
Периметр: 0
```

Результат: пройдено.

## M06 — python3 main.py circle 1

Ожидание: Площадь: 3.141592654; Периметр: 6.283185307. Код завершения: 0.

```text
Площадь: 3.141592654
Периметр: 6.283185307
```

Результат: пройдено.

## M07 — python3 main.py circle 0

Ожидание: Площадь: 0; Периметр: 0. Код завершения: 0.

```text
Площадь: 0
Периметр: 0
```

Результат: пройдено.

## M08 — python3 main.py triangle 3 4 5

Ожидание: Площадь: 6; Периметр: 12. Код завершения: 0.

```text
Площадь: 6
Периметр: 12
```

Результат: пройдено.

## M09 — python3 main.py triangle 1 2 3

Ожидание: Сумма двух сторон должна быть больше третьей. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: Сумма двух сторон должна быть больше третьей
```

Результат: пройдено.

## M10 — python3 main.py rectangle -1 4

Ожидание: Размер должен быть конечным числом. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: Размер должен быть конечным числом от 0 до 1000000000
```

Результат: пройдено.

## M11 — python3 main.py square nan

Ожидание: Размер должен быть конечным числом. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: Размер должен быть конечным числом от 0 до 1000000000
```

Результат: пройдено.

## M12 — python3 main.py circle 1000000001

Ожидание: Размер должен быть конечным числом. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: Размер должен быть конечным числом от 0 до 1000000000
```

Результат: пройдено.

## M13 — python3 main.py rectangle 3

Ожидание: требуется размеров: 2. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: Для rectangle требуется размеров: 2
```

Результат: пройдено.

## M14 — python3 main.py square abc

Ожидание: invalid float value. Код завершения: 2.

```text
usage: main.py [-h] {rectangle,square,circle,triangle} sizes [sizes ...]
main.py: error: argument sizes: invalid float value: 'abc'
```

Результат: пройдено.

