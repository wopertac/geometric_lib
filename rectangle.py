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
        ([3, 4], 12, int),
        ([6, 10], 60, int),
        ([100, 99], 9900, int),
        ([3.5, 4.3], 15.049999999999999, float),
        ([25.4346, 20.2836], 515.90525256, float),
        ([1028.492749027, 10.2], 10490.626040075398, float),
        ([-6, -93], None, type(None)),
        ([-3.582, -82673], None, type(None))
    ]

    tests_perimeter = [
        ([3, 4], 14, int),
        ([6, 10], 32, int),
        ([100, 99], 398, int),
        ([3.5, 4.3], 15.6, float),
        ([25.4346, 20.2836], 91.43639999999999, float),
        ([1028.492749027, 10.2], 2077.385498054, float),
        ([-6, -93], None, type(None)),
        ([-3.582, -82673], None, type(None))
    ]

    def test_rectangle_area(self):
        for params, resExpected, resType in self.tests_area:
            result = area(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)

    def test_rectangle_perimeter(self):
        for params, resExpected, resType in self.tests_perimeter:
            result = perimeter(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)