correctness = False

while not correctness:
    user_ip = input('Введите IP: ').split('.')

    if len(user_ip) == 4:
        for el in user_ip:
            if not el.isdigit():
                print(el, '— это не целое число.\n')
                break
            elif 0 > int(el) or int(el) > 255:
                print(el, 'превышает 255 или пременьшает 0.\n')
                break
        else:
            correctness = True
    else:
        print('Адрес — это четыре числа, разделённые точками.\n')

    # if correctness == False:
    #     user_ip = input('Введите IP: ').split('.')

print('IP-адрес корректен.')
