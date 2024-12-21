def rectangleArea(a, b):
    '''Принимает 2 числа, a и b. a - первая сторона прямоугольника, b - вторая сторона прямоугольника. Возвращает площадь прямоугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами.")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return a * b


def rectanglePerimeter(a, b):
    '''Принимает 2 числа a и b. a - первая сторона прямоугольника, b - вторая сторона прямоугольника. Возвращает периметр прямоугольника.'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами.")
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными.")
    return (a + b) * 2
