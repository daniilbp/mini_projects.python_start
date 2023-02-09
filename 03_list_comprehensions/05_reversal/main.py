text = input('Введите строку: ')

L_h = text.find('h')
R_h = text.rfind('h')

if L_h == -1:
    print('В строке нет символов h.')

elif L_h == R_h:
    print('В строке только один символов h.')

else:
    new_text = text[L_h + 1:R_h]
    print('Развёрнутая последовательность между первым и последним h:', new_text[::-1])
