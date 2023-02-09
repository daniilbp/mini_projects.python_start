def sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]

rollers, foots = [], []
N = int(input('\nКол-во коньков: '))
for elem in range(1, N + 1):
    print('Размер', elem, '-й пары:', end = ' ')
    size_roll = int(input())
    rollers.append(size_roll)
sort(rollers)

K = int(input('Кол-во людей: '))
for elem in range(1, K + 1):
    print('Размер ноги', elem, '-ого человека:', end = ' ')
    size_foot = int(input())
    foots.append(size_foot)
sort(foots)

count_people = 0

for people in foots:
    for roll in rollers:
        if people <= roll:
            count_people += 1
            rollers.remove(roll)

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_people)
