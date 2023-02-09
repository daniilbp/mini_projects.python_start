text = input('Введите текст: ').lower()

vowels =['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']

vowels_from_text = [sym for sym in text if sym in vowels]

print('\nСписок гласных букв:', vowels_from_text)
print('Длина списка:', len(vowels_from_text))
