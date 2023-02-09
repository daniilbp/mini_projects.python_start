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

for product in goods:
    sum_quantity, sum_price = 0, 0
    for i_list in range(len(store[goods[product]])):
        sum_quantity += store[goods[product]][i_list]['quantity']
        sum_price += store[goods[product]][i_list]['price'] * store[goods[product]][i_list]['quantity']

    print('{0} - {1} шт., стоимостью {2:,d} руб.'.format(
        product,
        sum_quantity,
        sum_price
    ))
