# Общее описание `geometric_lib`

# Описание функций
## `square.py`
### Площадь 
```py
def area(a : int|float) -> int|float:
    '''
    Вычисляет площадь квадрата со стороной a

    Параметры:
        a (int|float) - сторона квадрата

    Возвращает:
        S (int|float) - площадь квадрата

    '''
    return a * a
```

Пример вызова
```py
>>> import geometric_lib.square
>>> a = geometric_lib.square.area(3)
>>> print(type(a), a)
<class 'int'> 9
>>> b = geometric_lib.square.area(1.5)
>>> print(type(a), a)
<class 'float'> 2.25
```

### Периметр
```py
def perimeter(a : int|float) -> int|float:
    '''
    Вычисляет периметр квадрата со стороной а

    Параметры:
        a (int|float) - сторона квадрата

    Возвращает:
        P (int|float) - периметр квадрата
    '''
    return 4 * a
```

Пример вызова
```py
>>> import geometric_lib.square
>>> a = geometric_lib.square.perimeter(3)
>>> print(type(a), a)
<class 'int'> 12
>>> a = geometric_lib.square.perimeter(1.2)
>>> print(type(a), a)
<class 'float'> 4.8
>>>
```
## `circle.py`
### Площадь

```py
def area(r : int|float) -> float:
    '''
    Вычисляет площадь круга с радиусом r

    Параметры:
        r (int|float) - радиус круга

    Возвращает:
        S (int|float) - площадь круга
    '''
    return math.pi * r * r
```

Пример вызова

```py
>>> import geometric_lib.circle
>>> a = geometric_lib.circle.area(3)
>>> print(type(a), a)
<class 'float'> 28.274333882308138
```

### Периметр

```py
def perimeter(r : int|float) -> float:
    '''
    Вычисляет периметр круга с радиусом r

    Параметры:
        r (int|float) - радиус круга

    Возвращает:
        P (int|float) - периметр круга
    '''
    return 2 * math.pi * r
```

Пример вызова
```py
>>> import geometric_lib.circle
>>> a = geometric_lib.circle.perimeter(3)
>>> print(type(a), a)
<class 'float'> 18.84955592153876
```

# История изменения проекта
- Добавлены модули `square.py` `triangle.py` (smartiqa >`8ba9aeb3cea847b63a91ac378a2a6db758682460`)
- Добавлена документация используемых формул (smartiqa > `d078c8d9ee6155f3cb0e577d28d337b791de28e2`)
