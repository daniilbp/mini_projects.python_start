shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
count_detail, count_price = 0, 0

for elem in shop:
    if detail in elem:
        count_detail += 1
        count_price += elem[1]

print('Кол-во деталей -', count_detail)
print('Общая стоимость -', count_price)
