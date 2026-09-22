# Общее описание `geometric_lib`

Библиотека позволяет вычислять площадь и геометрических фигур:
- кладрат
- прямоугольник
- треугольник
- круг

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
## `rectangle.py`
### Площадь
```py
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
```
Пример вызова
```py
>>> import geometric_lib.rectangle
>>> a = geometric_lib.rectangle.area(3, 4)
>>> print(type(a), a)
<class 'int'> 12
>>> a = geometric_lib.rectangle.area(1.5, 2.5)
>>> print(type(a), a)
<class 'float'> 3.75
```
### Периметр
```py
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
```
Пример вызова
```py
>>> import geometric_lib.rectangle
>>> a = geometric_lib.rectangle.perimeter(3, 4)
>>> print(type(a), a)
<class 'int'> 14
>>> a = geometric_lib.rectangle.perimeter(1.5, 2.25)
>>> print(type(a), a)
<class 'float'> 7.5
```
## `triangle.py`
### Площадь
```py
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
```
Пример вызова
```py
>>> import geometric_lib.triangle
>>> a = geometric_lib.triangle.area(13, 14, 15)
>>> print(type(a), a)
<class 'float'> 84.0
```
### Периметр
```py
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
```
Пример вызова
```py
>>> import geometric_lib.triangle
>>> a = geometric_lib.triangle.area(13, 14, 15)
>>> print(type(a), a)
<class 'int'> 42
>>> a = geometric_lib.triangle.area(13.5, 14.5, 15.25)
>>> print(type(a), a)
<class 'float'> 43.25
```

# История изменения проекта
- Добавлены модули `square.py` `triangle.py` (smartiqa >`8ba9aeb3cea847b63a91ac378a2a6db758682460`)
- Добавлена документация используемых формул (smartiqa > `d078c8d9ee6155f3cb0e577d28d337b791de28e2`)
- Добавлена документация для `square.py` и `circle.py` (wopertac > `171a7fc0f59823fabb81207f5f9cc20a665e65f3`)
- Добавлены модули `rectangle.py` `triangle.py` (wopertac > `bd22b14611efe9070145f618cc9b759e03108490`)