count, players, dct = 0, 0, {}

with open('first_tour.txt', 'r') as file, open('second_tour.txt', 'w') as do_file:
    data = ' '.join(file.read().split('\n')).split(' ')

    for i in range(1, len(data), 3):
        if int(data[i+2]) > int(data[0]):
            name = data[i+1][:1] + '. ' + data[i]
            dct[data[i+2]] = name
            players += 1

    do_file.write(str(players) + '\n')

    for el in sorted(dct.keys())[::-1]:
        count += 1
        do_file.write(str(count) + ') ' + dct[el] + ' ' + str(el) + '\n')
