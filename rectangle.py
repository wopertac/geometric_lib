import unittest

def area(a : int|float, b : int|float) -> int|float:
    '''
    Вычисляет площадь прямоугольника со сторонами a, b
    
    Параметры:
        a (int|float) - первая сторона прямоугольника
        b (int|float) - вторая сторона прямугольникоа

    Возвращает:
        S (int|float) - площадь прямоугольника
    '''
    return a * b

def perimeter(a : int|float, b : int|float) -> int|float:
    '''
    Вычисляет периметр прямоугольника со сторонами а, b
    
    Параметры:
        a (int|float) - первая сторона прямоугольника
        b (int|float) - вторая сторона прямоугольника
    
    Возвращает:
        P (int|float) - периметр прямоугольника
    '''
    return 2 * (a + b)


class TestRectangleMethods(unittest.TestCase):

    tests_area = [
        ([3, 4], 12),
        ([6, 10], 60),
        ([100, 99], 9900),
        ([3.5, 4.3], 15.049999999999999),
        ([25.4346, 20.2836], 515.90525256),
        ([1028.492749027, 10.2], 10490.626040075398)
    ]

    tests_perimeter = [
        ([3, 4], 14),
        ([6, 10], 32),
        ([100, 99], 398),
        ([3.5, 4.3], 15.6),
        ([25.4346, 20.2836], 91.43639999999999),
        ([1028.492749027, 10.2], 2077.385498054)
    ]

    def test_area(self):
        for params, res in self.tests_area:
            self.assertEqual(area(*params), res)

    def test_perimeter(self):
        for params, res in self.tests_perimeter:
            self.assertEqual(perimeter(*params), res)