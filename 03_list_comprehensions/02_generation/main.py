N = int(input('Введите длину списка: '))

new_list = [1 if not num % 2 else num % 5 for num in range(N)]

print('Результат:', new_list)
