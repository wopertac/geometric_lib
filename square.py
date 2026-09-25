import unittest

def area(a : int|float) -> int|float:
    '''
    Вычисляет площадь квадрата со стороной a

    Параметры:
        a (int|float) - сторона квадрата

    Возвращает:
        S (int|float) - площадь квадрата

    '''
    return a * a


def perimeter(a : int|float) -> int|float:
    '''
    Вычисляет периметр квадрата со стороной а

    Параметры:
        a (int|float) - сторона квадрата

    Возвращает:
        P (int|float) - периметр квадрата
    '''
    return 4 * a


class TestSquareMethods(unittest.TestCase):

    tests_area = [
        ([3], 9, int),
        ([6], 36, int),
        ([100], 10000, int),
        ([3.5], 12.25, float),
        ([25.4346], 646.91887716, float),
        ([1028.492749027], 1057797.3348011156, float),
        ([-1], None, type(None)),
        ([-4.3], None, type(None))
    ]

    tests_perimeter = [
        ([3], 12, int),
        ([6], 24, int),
        ([100], 400, int),
        ([3.5], 14, int),
        ([25.4346], 101.7384, float),
        ([1028.492749027], 4113.970996108, float),
        ([-1], None, type(None)),
        ([-4.3], None, type(None))
    ]

    def test_square_area(self):
        for params, resExpected, resType in self.tests_area:
            result = area(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)

    def test_square_perimeter(self):
        for params, resExpected, resType in self.tests_perimeter:
            result = perimeter(*params)
            self.assertEqual(result, resExpected)
            self.assertEqual(type(result), resType)