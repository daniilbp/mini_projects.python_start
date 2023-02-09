user_str = input('Введите строку: ')
count = 1
cipher_str = ''

for sym in range(1, len(user_str)):
    if user_str[sym] == user_str[sym - 1]:
        count += 1
    else:
        cipher_str += user_str[sym - 1] + str(count)
        count = 1
    if sym == len(user_str) - 1:
        cipher_str += user_str[sym] + str(count)


print('Закодированная строка:', cipher_str)
