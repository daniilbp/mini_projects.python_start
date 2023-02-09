user_text = input('Сообщение: ')
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

new_text = []
part_text = []

for sym in user_text:
    if sym.lower() in alphabet:
        part_text.append(sym)
    else:
        new_text.extend(part_text[::-1])
        new_text.append(sym)
        part_text = []

print('Новое сообщение:', ''.join(new_text))
