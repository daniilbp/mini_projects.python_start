import  random

res, probability = 0, 0
errors = ['Вас постигла неудача!', 'the E-R-R-O-R', 'Что-то пошло не так', 'В следующий раз повезет, возможно...']

with open('out_file.txt', 'w') as file:
    while res < 777:
        user_num = int(input('Введите число: '))
        res += user_num
        probability += 1
        try:
            if random.randint(1, 13) == probability % 13:
                raise SystemError
            file.write(str(user_num) + '\n')
        except SystemError:
            print(random.choice(errors))
            break
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
