main = [1, 5, 3]
dop_1 = [1, 5, 1, 5]
dop_2 = [1, 3, 1, 5, 3, 3]

main.extend(dop_1)

print('Кол-во цифр 5 при первом объединении:', main.count(5))

while 5 in main:
    main.remove(5)

main.extend(dop_2)

print('Кол-во цифр 3 при втором объединении:', main.count(3))

print('Итоговый список', main)
