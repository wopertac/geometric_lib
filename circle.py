import math


def area(r : int|float) -> float:
    '''
    Вычисляет площадь круга с радиусом r

    Параметры:
        r (int|float) - радиус круга

    Возвращает:
        S (int|float) - площадь круга
    '''
    return math.pi * r * r


def perimeter(r : int|float) -> float:
    '''
    Вычисляет периметр круга с радиусом r

    Параметры:
        r (int|float) - радиус круга

    Возвращает:
        P (int|float) - периметр круга
    '''
    return 2 * math.pi * r

