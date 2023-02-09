user_str = input('Введите строку: ')

words_list = user_str.split()

max_lenght = ''
for word in words_list:
    if len(word) > len(max_lenght):
        max_lenght = word

print('Самое длинное слово:', max_lenght)
print('Длина этого слова:', len(max_lenght))
