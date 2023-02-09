num_str = int(input('Сколько записей вносится в протокол? '))
players_dict = {}
count = 0
winners_set = set([])

print('Записи (результат и имя):')

for num in range(1, num_str + 1):
    record = input('{0}-я запись: '.format(num)).split()
    if int(record[0]) in players_dict:
        players_dict[int(record[0])].append(record[1])
    else:
        players_dict.update({int(record[0]): [record[1]]})

print('\nИтоги соревнований:')

for el in sorted(players_dict.keys())[::-1]:
    for i in players_dict[el]:
        if i not in winners_set and count < 3:
            count += 1
            print('{0}-е место.'.format(count), i, '({0})'.format(el))
            winners_set.add(i)
    if count == 3:
        break
