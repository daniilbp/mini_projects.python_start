## Цели практической работы
- Отработать представление информации в Python в виде словаря и множества.
- Научиться:
  - инициализировать пустой словарь и заполнять его парами «ключ— значение», генерировать словарь;
  - работать с ключами и значениями словаря: получать значение по ключу, обновлять значение, удалять запись по ключу, выводить значение на экран;
  - получать отображения списков ключей и значений словаря и использовать их для обработки словаря;
  - работать со вложенными словарями, получать/изменять/удалять значения;
  - инициализировать множества и выполнять с ними математические действия, такие как пересечение, объединение и разность.
## Что входит в работу
- Задача 1. Песни 2.
- Задача 2. География.
- Задача 3. Криптовалюта.
- Задача 4. Товары.
- Задача 5. Гистограмма частоты 2.
- Задача 6. Словарь синонимов.
- Задача 7. Пицца.
- Задача 8. Угадай число.
- Задача 9. Родословная.
- Задача 10. Снова палиндром.

В тех задачах, где не дан начальный формат данных (например, в задаче 1 уже есть готовый словарь), для решения необходимо использовать словари и/или множества.
## Задача 1. Песни 2
### Что нужно сделать
Мы продолжаем писать приложение для удобного прослушивания музыки, но теперь наши песни хранятся в виде словаря, а не вложенных списков. Каждая песня состоит из названия и продолжительности с точностью до долей минут.

```python
violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
```

Напишите программу, которая запрашивает у пользователя количество песен из списка и названия этих песен, а на экран выводит общее время их звучания.

Пример:

```
Сколько песен выбрать? 3
Название первой песни: Halo
Название второй песни: Enjoy the Silence
Название третьей песни: Clean

Общее время звучания песен: 14.93 минуты
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 2. География
### Что нужно сделать
Антон, помимо программирования, также увлекается и географией, поэтому он решил связать эти две области и написать для своего проекта небольшую программу-навигатор.

Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся, в одну строку. После пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.

Пример: 

```
Количество стран: 2
Первая страна: Россия Москва Петербург Новгород
Вторая страна: Германия Берлин Лейпциг Мюнхен

Первый город: Москва
Город Москва расположен в стране Россия.

Второй город: Мюнхен
Город Мюнхен расположен в стране Германия.

Третий город: Рим
По городу Рим данных нет.
```

### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует указанному в задаче.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 3. Криптовалюта
### Что нужно сделать
При работе с API (application programming interface) сайта биржи по криптовалюте вы получили вот такие данные в виде словаря:

```python
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
```

Теперь вам предстоит немного обработать эти данные.

Напишите программу, которая выполняет следующий алгоритм действий:

1. Вывести списки ключей и значений словаря.
1. В “ETH” добавить ключ “total_diff” со значением 100.
1. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
1. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
1. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.

После выполнения алгоритма выводить результат (словарь) не нужно.
### Что оценивается
- Результат вычислений корректен.
- В коде соблюдается порядок действий алгоритма.
- Не используется других переменных, кроме data.
## Задача 4. Товары
### Что нужно сделать
В базе данных магазина вся необходимая информация по товарам делится на два словаря: первый отвечает за коды товаров, второй — за списки количества разнообразных товаров на складе:

```python
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
```

Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за одну штуку).

Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.

Результат работы программы:

```
Лампа — 27 штук, стоимость 1134 рубля
Стол — 54 штуки, стоимость 27 860 рублей
Диван — 3 штуки, стоимость 3550 рублей
Стул — 105 штук, стоимость 10 311 рублей
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует указанному в задаче.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 5. Гистограмма частоты 2
### Что нужно сделать
Мы уже писали программу для лингвистов, которая получала на вход текст и считала, сколько раз в строке встречается каждый символ. Теперь задача немного поменялась: максимальную частоту выводить не нужно, однако необходимо написать функцию, которая будет инвертировать полученный словарь. То есть в качестве ключа будет частота, а в качестве значения — список символов с этой частотой. Реализуйте такую программу.

Пример:

```
Введите текст: здесь что-то написано
Оригинальный словарь частот:
  : 2
- : 1
З : 1
а : 2
д : 1
е : 1
и : 1
н : 2
о : 3
п : 1
с : 2
т : 2
ч : 1
ь : 1

Инвертированный словарь частот:
1 : ['З', 'д', 'е', 'ь', 'ч', '-', 'п', 'и']
2 : ['с', ' ', 'т', 'н', 'а']
3 : ['о']
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельных функциях.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 6. Словарь синонимов
### Что нужно сделать
Одна библиотека поручила вам написать программу для оцифровки словарей синонимов. На вход в программу подаётся N пар слов. Каждое слово является синонимом к своему парному слову. 

Реализуйте код, который составляет словарь синонимов (все слова в словаре различны), затем запрашивает у пользователя слово и выводит на экран его синоним. Обеспечьте контроль ввода: если такого слова нет, то выведите ошибку и запросите слово ещё раз. При этом проверка не должна зависеть от регистра символов.

Пример:

```
Введите количество пар слов: 3
Первая пара: Привет — Здравствуйте
Вторая пара: Печально — Грустно
Третья пара: Весело — Радостно

Введите слово: интересно
Такого слова в словаре нет.
Введите слово: здравствуйте
Синоним: Привет
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 7. Пицца
### Что нужно сделать
В базе данных интернет-магазина PizzaTime хранятся данные о том, кто, что и сколько заказывал у них в определённый период. Вам нужно структурировать эту информацию, а также понять, сколько всего пицц купил каждый заказчик.

На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название пиццы — количество заказанных пицц». Реализуйте код, который выводит список покупателей и их заказов по алфавиту. Учитывайте, что один человек может заказать одно и то же несколько раз.

Пример:

```
Введите количество заказов: 6
Первый заказ: Иванов Пепперони 1
Второй заказ: Петров Де-Люкс 2
Третий заказ: Иванов Мясная 3
Четвёртый заказ: Иванов Мексиканская 2
Пятый заказ: Иванов Пепперони 2
Шестой заказ: Петров Интересная 5

Иванов: 
	Мексиканская: 2
	Мясная: 3
	Пепперони: 3
Петров:
	Де-Люкс: 2
	Интересная: 5
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру (перед названием пиццы пять пробелов).
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 8. Угадай число
### Что нужно сделать
Артём и Борис играют в игру. Артём загадал натуральное число от 1 до N. Борис пытается угадать это число, для этого он называет несколько чисел подряд. Артём говорит Борису «да», если среди названных Борисом чисел есть задуманное. В противном случае Артём говорит «нет». После нескольких заданных вопросов Борис сдался и попросил вас помочь ему определить, какие числа мог задумать Артём.

Напишите программу, которая имитирует диалог Артёма и Бориса. В начале на вход подаётся число N — это максимальное число, которое мог загадать Артём. Затем Борис предполагает, что среди некоторых чисел есть то, которое загадал Артём (несколько чисел через пробел), а Артём отвечает. Так продолжается до тех пор, пока Борис не попросит помощи (пока не введётся строка «Помогите!»). В конце программы необходимо вывести, какие числа мог загадать Артём.

Пример реализации:

```
Введите максимальное число: 10

Нужное число есть среди вот этих чисел: 1 2 3 4 5
Ответ Артёма: Да

Нужное число есть среди вот этих чисел: 2 4 6 8 10
Ответ Артёма: Нет

Нужное число есть среди вот этих чисел: Помогите!
Артём мог загадать следующие числа: 1 3 5
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 9. Родословная
### Что нужно сделать
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждому элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого элемента высота на один больше, чем у его родителя. Вам нужно написать программу, которая по заданному генеалогическому древу определяет высоту всех его элементов.

Программа получает на вход N количество человек в генеалогическом древе. Далее следует N − 1 строк, в каждой из которых задаётся родитель для каждого элемента дерева, кроме родоначальника. Каждая строка имеет вид «имя_потомка имя_родителя».

Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту). После вывода имени каждого элемента необходимо вывести его высоту.

Пример:

```
Введите количество человек: 9
Первая пара: Alexei Peter_I
Вторая пара: Anna Peter_I
Третья пара: Elizabeth Peter_I
Четвёртая пара: Peter_II Alexei
Пятая пара: Peter_III Anna
Шестая пара: Paul_I Peter_III
Седьмая пара: Alexander_I Paul_I
Восьмая пара: Nicholaus_I Paul_I

«Высота» каждого члена семьи:
Alexander_I 4
Alexei 1
Anna 1
Elizabeth 1
Nicholaus_I 4
Paul_I 3
Peter_I 0
Peter_II 2
Peter_III 2
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).
## Задача 10. Снова палиндром
### Что нужно сделать
Пользователь вводит строку. Необходимо написать программу, которая определяет, существует ли у этой строки такая перестановка, при которой она станет палиндромом. Выведите соответствующее сообщение.

Пример 1:

```
Введите строку: aab
Можно сделать палиндромом
```

Пример 2:

```
Введите строку: aabc
Нельзя сделать палиндромом
```
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Формат вывода соответствует примеру.
- Основной функционал описан в отдельной функции(-ях)
- Переменные и функции имеют значащие имена, не только a, b, c, d (подробнее об этом в видео 2.3).

