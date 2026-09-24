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
        ([3], 9),
        ([6], 36),
        ([100], 10000),
        ([3.5], 12.25),
        ([25.4346], 646.91887716),
        ([1028.492749027], 1057797.3348011156)
    ]

    tests_perimeter = [
        ([3], 12),
        ([6], 24),
        ([100], 400),
        ([3.5], 14),
        ([25.4346], 101.7384),
        ([1028.492749027], 4113.970996108)
    ]

    def test_area(self):
        for params, res in self.tests_area:
            self.assertEqual(area(*params), res)

    def test_perimeter(self):
        for params, res in self.tests_perimeter:
            self.assertEqual(perimeter(*params), res)