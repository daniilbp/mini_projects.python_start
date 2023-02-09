# def cipher(letter, K, alphabet):
#     new_letter = ''
#     for i_num in range(len(alphabet)):
#         if alphabet[i_num] == letter:
#             new_letter = alphabet[(i_num + K) % len(alphabet)]
#             break
#     return new_letter

mail = input('Введите сообщение: ')
K = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# new_mail = [cipher(letter, K, alphabet) if letter in alphabet else letter for letter in mail]

new_mail = [alphabet[(alphabet.find(letter) + K) % len(alphabet)] if letter in alphabet else letter for letter in mail]

print('Зашифрованное сообщение:', end = ' ')
for sym in new_mail:
    print(sym, end = '')
