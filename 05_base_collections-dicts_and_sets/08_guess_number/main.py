max_num = int(input('Введите максимальное число: '))
possible_options = set([el for el in range(max_num + 1)])
artem_num = 3

attempt = input('\nНужное число есть среди вот этих чисел: ')

while attempt != 'Помогите!':
    attempt_set = set([])
    attempt_list = attempt.split()
    for num in attempt_list:
        attempt_set.add(int(num))

    if artem_num in attempt_set:
        print('Ответ Артёма: Да')
        possible_options = possible_options & attempt_set
    else:
        print('Ответ Артёма: Нет')
        possible_options = possible_options - attempt_set

    attempt = input('\nНужное число есть среди вот этих чисел: ')

print('Артём мог загадать следующие числа:', end = ' ')
for info in sorted(possible_options):
    print(int(info), end = ' ')
