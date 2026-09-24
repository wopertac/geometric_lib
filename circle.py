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
        ([3], 28.274333882308138),
        ([6], 113.09733552923255),
        ([100], 31415.926535897932),
        ([3.5], 38.48451000647496),
        ([25.4346], 2032.3555919544137),
        ([1028.492749027], 3323168.3359980476)
    ]

    tests_perimeter = [
        ([3], 18.84955592153876),
        ([6], 37.69911184307752),
        ([100], 628.3185307179587),
        ([3.5], 21.991148575128552),
        ([25.4346], 159.8103050139899),
        ([1028.492749027], 6462.210529227188)
    ]

    def test_area(self):
        for params, res in self.tests_area:
            self.assertEqual(area(*params), res)

    def test_perimeter(self):
        for params, res in self.tests_perimeter:
            self.assertEqual(perimeter(*params), res)