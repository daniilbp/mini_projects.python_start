def divider(n):
    for num in range (2, n + 1):
        if not n % num:
            break
    return num

n = int(input('ВВедите число: '))
min_divider = divider(n)
print('Наименьший делитель, отличный от единицы:', min_divider)
