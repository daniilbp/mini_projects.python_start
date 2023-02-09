def check_symmetry(my_list):
    is_symmetry = True

    for i in range(len(my_list) // 2):
        if my_list[i] != my_list[-1 - i]:
            is_symmetry = False
            break

    return is_symmetry

my_list, new_list = [], []
N = int(input('Кол-во чисел: '))

for _ in range(N):
    number = int(input('Число: '))
    my_list.append(number)

print('\nПоследовательность:', my_list)

is_symmetry = check_symmetry(my_list)

if is_symmetry:
    print('Последовательность симмтричная, приписывать ничего не надо.')
else:
    for i in range(1, len(my_list)):
        for s in range(len(my_list) - i):
            if my_list[i + s] != my_list[-1 - s]:
                break
        else:
            break
    print('Нужно приписать чисел:', i)

    for i_el in range(i - 1, -1, -1):
        new_list.append(my_list[i_el])

    print('Сами числа:', new_list)
