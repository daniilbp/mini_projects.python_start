import random

N = int(input('Количество палок: '))
stick_list = ['I' for _ in range(N)]

K = int(input('Количество бросков: '))

for num in range(K):
    L_i = random.randint(1, N)
    R_i = random.randint(L_i, N)
    print('Бросок', num + 1, '. Сбиты палки с номера', L_i, '\nпо номер', R_i, '.')
    for el in range(L_i - 1, R_i):
        stick_list[el] = '.'

print('\nРезультат:', end = ' ')
for sym in stick_list:
    print(sym, end ='')
