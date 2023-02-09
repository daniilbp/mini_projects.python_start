def counter(number):
    if number:
        counter(number - 1)
        print(number)

num = int(input('Введите num: '))
counter(num)
