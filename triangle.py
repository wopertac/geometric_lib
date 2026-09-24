import unittest

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

class TestTriangleMethods(unittest.TestCase):

    tests_area = [
        ([3, 4, 5], 6),
        ([6, 10, 14], 25.98076211353316),
        ([100, 99, 98], 4243.091377462899),
        ([3.5, 4.3, 6.4], 7.077965809468137),
        ([12.3456, 15.7891, 19.1112], 97.03551927471611),
        ([1234.56789101, 2345.67891011, 3456.78910112], 762757.5015345167)
    ]

    tests_perimeter = [
        ([3, 4, 5], 12),
        ([6, 10, 14], 30),
        ([100, 99, 98], 297),
        ([3.5, 4.3, 6.4], 14.2),
        ([12.3456, 15.7891, 19.1112], 47.2459),
        ([1234.56789101, 2345.67891011, 3456.78910112], 7037.03590224)
    ]

    def test_area(self):
        for params, res in self.tests_area:
            self.assertEqual(area(*params), res)

    def test_perimeter(self):
        for params, res in self.tests_perimeter:
            self.assertEqual(perimeter(*params), res)