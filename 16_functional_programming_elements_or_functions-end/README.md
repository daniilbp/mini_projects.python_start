## Цели практической работы
- Закрепить понятия «пространство имён» и «область видимости» и работу с ними, использование `global` и `nonlocal`.
- Отработать создание и использование лямбда-функций, в том числе встроенных в Python.
- Отработать использование блока `if __name__ == "__main__"` для чистоты кода.
## Что входит в работу
- Задача 1. Новые списки.
- Задача 2. И снова zip.
- Задача 3. Читабельность кода.
- Задача 4. Палиндром: возвращение.

## Задача 1. Новые списки
### Что нужно сделать
Даны три списка: 

```python
from typing import List


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
```

Напишите код, который создаёт три новых списка. Вот их содержимое:

1. Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
1. Из списка names берутся только те имена, в которых есть минимум пять букв.
1. Из списка numbers берётся произведение всех чисел.
### Что оценивается
- Результат вычислений корректен.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Решение опирается на использование лямбда-функций.

## Задача 2. И снова zip
### Что нужно сделать
Помните, как нам приходилось что-то выдумывать, чтобы создать аналог функции zip? Так вот, теперь вы знаете, как это сделать буквально в одну строку.

Даны список букв (letters) и список цифр (numbers). Каждый список состоит из N элементов. Создайте кортежи из пар элементов списков и запишите их в список results. Не используйте функцию zip. Решите задачу «в одну строку» (не считая print(results)).

Пример списков:
```python
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
```

Результат работы программы:
```
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Решение опирается на использование лямбда-функций

## Задача 3. Читабельность кода
### Что нужно сделать
Необходимо вывести на экран список простых чисел от 0 до 1000. Реализуйте это двумя способами: 

1) «однострочным» кодом, без объявления дополнительных функций;
1) обычным, «своим» кодом, который покажется вам наиболее красивым.

После этого ответьте себе (не куратору) на вопрос: какое из решений более читабельное?
### Что оценивается
- Результат вычислений корректен.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Решение опирается на использование лямбда-функций.

## Задача 4. Палиндром: возвращение
### Что нужно сделать
Для Python существует множество различных библиотек для работы с данными, причём как встроенных, так и внешних. С некоторыми из них мы уже работали, например с модулем `collections`, когда использовали специальный класс `OrderedDict`, с помощью которого делали упорядоченный словарь. Конечно же, в этой библиотеке есть и другие возможности (на самом деле их совсем немного). Вот официальная документация: [collections — Container datatypes](https://docs.python.org/3/library/collections.html).

Используя модуль `collections` и новые знания о функциях, реализуйте функцию `can_be_poly`, которая принимает на вход строку и проверяет, можно ли получить из неё палиндром. 

Пример кода:
```python
print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
```

Результат:
```
True
False
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Решение опирается на использование лямбда-функций.
- Классы и методы/функции имеют прописанную документацию (хотя бы минимальную).
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.
