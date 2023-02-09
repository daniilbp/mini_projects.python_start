import os

def cipfer_cesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''.join([alphabet[(alphabet.find(el) + shift) % len(alphabet)] if el in alphabet else el for el in text.lower()])
    return new_text

def write_fun(info, num):
    new_text = cipfer_cesar(info, num)

    if os.path.exists(os.path.abspath('cipher_text.txt')):
        file = open('cipher_text.txt', 'a')
    else:
        file = open('cipher_text.txt', 'w')
    file.write(new_text.title())
    file.close()

def read_fun():
    shift = 0

    with open('text.txt', 'r') as file:
        for el in file:
            shift += 1
            write_fun(el, shift)

with open('text.txt', 'w') as file_from:
    for _ in range(4):
        file_from.write('Hello\n')

read_fun()
