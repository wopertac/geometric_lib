def area(a : int|float, b : int|float, c : int|float) -> float:
    '''
    Вычисляет площадь треугольника со сторонами a, b, c

    Параметры:
        a (int|float) - сторона треугольника
        b (int|float) - сторона треугольника
        c (int|float) - сторона треугольника

    Возвращает:
        S (int|float) - площадь треугольника
    '''

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** .5

def perimeter(a: int|float, b : int|float, c : int|float) -> int|float:
    '''
    Вычисляет периметр треугольника со сторонами a, b, c

    Параметры:
        a (int|float) - сторона треугольника
        b (int|float) - сторона треугольника
        c (int|float) - сторона треугольника

    Возвращает:
        P (int|float) - периметр треугольника
    '''
    
    return a + b + c