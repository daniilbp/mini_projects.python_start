import math

def detected(x, y, r):
    if r >= math.sqrt(x**2 + y**2):
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')

x = float(input('Введите координаты монетки:\nX: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
detected(x, y, r)
