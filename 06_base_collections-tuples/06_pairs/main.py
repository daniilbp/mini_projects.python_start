import random

random_list = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список:', random_list)

# v1
new_list = [(random_list[el], random_list[el + 1]) for el in range(0, len(random_list), 2)]
print('Новый список:', new_list)

# v2
random_list_first_half = random_list[0:len(random_list) + 1:2]
random_list_second_half = random_list[1:len(random_list) + 1:2]
new_list_v2 = list(zip(random_list_first_half, random_list_second_half))
print('Новый список v2:', new_list_v2)