num_pair = int(input('Введите количество пар слов: '))
pair_dict = {}

for num in range(1, num_pair + 1):
    pair = input('{0}- я пара: '.format(num)).split(' — ')
    pair_dict.update({pair[0]: pair[1], pair[1]: pair[0]})

print()
while True:
    word = input('Введите слово: ').title()

    if word in pair_dict:
        print('Синоним:', pair_dict.get(word))
        break

    else:
        print('Такого слова в словаре нет.')
