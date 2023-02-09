def rhyme(K, round):
    start_count = 0

    while len(round) > 1:

        print('\nТекущий круг людей:', round)
        print('Начало счёта с номера', round[start_count % len(round)])

        start_count = (start_count + K % len(round) - 1) % len(round)

        print('Выбывает человек под номером', round[start_count])
        round.remove(round[start_count])

        if start_count < 0:
            start_count = abs(start_count) - 1

    print('\nОстался человек под номером', round[start_count])

N = int(input('Кол-во человек: '))
round = list(range(1, N + 1))

K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, '-й человек')

rhyme(K, round)
