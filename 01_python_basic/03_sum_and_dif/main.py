def summa_numbers(N):
    summa = 0
    while N != 0:
        summa += N % 10
        N //= 10
    print('\nСумма чисел:', summa)
    return summa

def count_numbers(N):
    count = 0
    while N != 0:
        count += 1
        N //= 10
    print('Количество цифр в числе:', count)
    return count

N = int(input('Введите число: '))
summa = summa_numbers(N)
count = count_numbers(N)
print('Разность суммы и количества цифр:', summa - count)
