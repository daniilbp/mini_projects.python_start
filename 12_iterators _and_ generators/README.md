## Цель практической работы
- Закрепить понятия «итератор» и «генератор», отработать использование методов iter и next.
- Отработать умение создавать классы-итераторы и функции-генераторы, генераторные выражения.
- Отработать использование аннотации типов.
## Что входит в задание
- Задача 1. Квадраты чисел.
- Задача 2. Рефакторинг.
- Задача 3. Пути файлов.
- Задача 4. Последовательность Хофштадтера.
- Задача 5. Количество строк.
- Задача 6. Односвязный список.
- 
## Задача 1. Квадраты чисел
### Что нужно сделать
Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N (`1 ** 2`, `2 ** 2`, `3 ** 2` и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 2. Рефакторинг
### Что нужно сделать
После различных вопросов про различия итераторов, генераторов и генераторных выражений на собеседовании вам дали небольшой пример кода и попросили «провести рефакторинг». Вот сам код:

```python
# Нужно найти, какие два числа из списков в результате попарного перемножения дадут число 56.
list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break
```
Проблема кода состоит в некрасивом выходе из циклов (два `break` и флаг). Реализуйте более красивый выход из циклов, используя генератор. Сам алгоритм решения (попарное перемножение) и списки трогать нельзя.
### Что оценивается
- Результат вычислений корректен.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 3. Пути файлов
### Что нужно сделать
Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов. 

**Подсказка:**

Существует функция, которая может получать все имена файлов в дереве каталогов. Попробуйте найти ее самостоятельно.

### Что оценивается
- Результат вычислений корректен.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 4. Последовательность Хофштадтера
### Что нужно сделать
Реализуйте генерацию последовательности Q Хофштадтера (итератором или генератором). Сама последовательность выглядит так:

`Q(n)=Q(n−Q(n−1))+Q(n−Q(n−2))`

В итератор (или генератор) передаётся список из двух чисел. Например, `QHofstadter([1, 1])` генерирует точную последовательность Хофштадтера. Если передать значения `[1, 2]`, то последовательность должна немедленно завершиться.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 5. Количество строк
### Что нужно сделать
Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет общее количество строк кода, игнорируя пустые строки и строчки комментариев. 
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 6. Односвязный список
### Что нужно сделать
Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.

Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.

![](06_linked_list/linkedlist.PNG)

В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:

- append — добавление элемента в конец списка;
- get — получение элемента по индексу;
- remove — удаление элемента по индексу.

Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:

```python
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
```

Результат:
```
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]
```
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.