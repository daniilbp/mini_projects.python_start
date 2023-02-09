def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibonacci(num_pos))
