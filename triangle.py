def traingleArea(a, h):
    '''Принимает 2 значения, a и h. a - сторона треугольника, h - высота, проведенная к стороне a. Возвращает площадь треугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Сторона и высота должны быть числами.")
    if a < 0 or h < 0:
        raise ValueError("Сторона и высота не могут быть отрицательными.")
    return a * h / 2


def trainglePerimeter(a, b, c):
    '''Принимает 3 значения, a, b и c. a - первая сторона треугольника, b - вторая сторона треугольника, c - третья сторона треугольника. Возвращает периметр треугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все стороны должны быть числами.")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return a + b + c
