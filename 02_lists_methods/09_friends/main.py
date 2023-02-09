N = int(input('Кол-во друзей: '))
friends = list(range(1, N + 1))

for i_el in friends:
    friends[i_el - 1] = 0

K = int(input('Долговых расписок: '))

for rec in range(1, K + 1):
    print()
    print(rec, '-я расписка')
    taking = int(input('Кому: '))
    giving = int(input('От кого: '))
    money = int(input('Сколько: '))

    friends[taking - 1] -= money
    friends[giving - 1] += money

print('\nБаланс друзей:')
for num_frnd in range(1, N + 1):
    print(num_frnd, ':', friends[num_frnd - 1])
