import random

random_list = [random.randint(0, 2) for _ in range(int(input('Количество чисел в списке: ')))]
print('Список до сжатия', random_list)

for el in range(len(random_list)):
    if random_list[el] == 0:
        random_list.append(random_list[el])
        random_list.remove(random_list[el])

final_list = [el for el in random_list if el != 0]

# without_zero_random_list = [el for el in random_list if el != 0]
# final_list = without_zero_random_list[:]
# zero_random_list = [el for el in random_list if el == 0]
# without_zero_random_list.extend(zero_random_list)

print('Список после сжатия', final_list)
