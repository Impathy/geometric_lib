def squareArea(a):
    '''Принимает 1 значение а. а - сторона квадрата. Возвращает площадь квадрата.'''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return a * a


def squarePerimeter(a):
    '''Принимает 1 значение а. а - сторона квадрата. Возвращает периметр квадрата.'''
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return 4 * a
