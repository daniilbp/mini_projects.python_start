from typing import List


# *v1 filter + lambda - сложно читабельно
print(list(filter(lambda el: el >= 2 and (el == 2 or all(el % i for i in range(2, el))), [num for num in range(0, 1001)])))

# **v2 list comprehensions - впринципе тоже приемлимо, но чуть сложнее пошаговость чем в v3
print([n for n in range(1000) if n >= 2 and (n == 2 or all(n % i for i in range(2, n)))])

# ***v3 более читабельное, простота в пошаговости
def is_prime(num: int) -> List[int]:
    prime_list = []
    user_list = [el for el in range(2, num + 1)]
    for number in user_list:
        for i_num in range(2, number):
            if number % i_num == 0:
                break
        else:
            prime_list.append(number)

    return prime_list

print(is_prime(1000))
