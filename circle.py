import math
import unittest

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

class TestCircleMethods(unittest.TestCase):

    tests_area = [
        ([3], 28.274333882308138, float),
        ([6], 113.09733552923255, float),
        ([100], 31415.926535897932, float),
        ([3.5], 38.48451000647496, float),
        ([25.4346], 2032.3555919544137, float),
        ([1028.492749027], 3323168.3359980476, float),
        ([-1], None, type(None)),
        ([-5.24], None, type(None))
    ]

    tests_perimeter = [
        ([3], 18.84955592153876, float),
        ([6], 37.69911184307752, float),
        ([100], 628.3185307179587, float),
        ([3.5], 21.991148575128552, float),
        ([25.4346], 159.8103050139899, float),
        ([1028.492749027], 6462.210529227188, float),
        ([-1], None, type(None)),
        ([-5.24], None, type(None))
    ]

    def test_circle_area(self):
        for params, resExpected, resType in self.tests_area:
            result = area(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)

    def test_circle_perimeter(self):
        for params, resExpected, resType in self.tests_perimeter:
            result = perimeter(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)