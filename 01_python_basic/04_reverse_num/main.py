def cut(text):
    temporary = ''
    for symbol in text:
        if symbol == '.':
            break
        temporary += symbol
    return temporary

def reverse(text):
    temporary = ''
    for symbol in text:
        temporary = symbol + temporary
    return temporary

N = input('Введите первое число: ')
N_whole = cut(N)
N_whole_reverse = reverse(N_whole)
N_reverse = reverse(N)
N_fraction_reverse = cut(N_reverse)
N_reverse = float(N_whole_reverse + '.' + N_fraction_reverse)

K = input('Введите второе число: ')
K_whole = cut(K)
K_whole_reverse = reverse(K_whole)
K_reverse = reverse(K)
K_fraction_reverse = cut(K_reverse)
K_reverse = float(K_whole_reverse + '.' + K_fraction_reverse)

print('\nПервое число наоборот:', N_reverse)
print('Второе число наоборот:', K_reverse)
print('Сумма:', N_reverse + K_reverse)
