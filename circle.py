import math


def circleArea(r):
    '''Принимает 1 значение r. r - радиус окружности. Возвращает площадь окружности.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом.")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * r * r


def circlePerimeter(r):
    '''Принимает 1 значение r. r - радиус окружности. Возвращает периметр окружности.'''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом.")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным.")
    return math.pi * r * 2
