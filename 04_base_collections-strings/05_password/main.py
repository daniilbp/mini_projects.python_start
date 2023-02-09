
while True:
    user_password = input('Придумайте пароль: ')
    count_num, count_isup = 0, 0

    for sym in user_password:
        if sym.isupper():
            count_isup += 1
        elif sym.isdigit():
            count_num += 1

    if len(user_password) >= 8 and count_isup >= 1 and count_num >= 3:
        print('Это надёжный пароль!')
        break

    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
