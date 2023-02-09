num_list_1, num_list_2 = [], []

for num_1 in range(1, 4):
    print('Введите', num_1, '-е число для первого списка:', end = ' ')
    num_for_l_1 = int(input())
    num_list_1.append(num_for_l_1)

for num_2 in range(1, 8):
    print('Введите', num_2, '-е число для второго списка:', end = ' ')
    num_for_l_2 = int(input())
    num_list_2.append(num_for_l_2)

print('\nПервый список:', num_list_1)
print('Второй список:', num_list_2)

num_list_1.extend(num_list_2)

for elem in num_list_1:
    while num_list_1.count(elem) > 1:
        num_list_1.remove(elem)

print('\nНовый первый список с уникальными элементами:', num_list_1)
