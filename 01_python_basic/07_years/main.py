year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))

print('\nГоды от', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
for num in range(year1, year2 + 1):
    num4 = num % 10
    temporary = num // 10
    num3 = temporary % 10
    temporary //= 10
    num2 = temporary % 10
    num1 = temporary // 10
    if num1 == num2 == num3 or num1 == num2 == num4 or num1 == num3 == num4 or num2 == num3 == num4:
        print(num)
