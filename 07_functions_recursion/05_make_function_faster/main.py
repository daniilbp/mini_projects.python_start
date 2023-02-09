def calculating_math_func(data, dct_fact=dict()):
    if data in dct_fact:
        result = dct_fact[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        dct_fact[data] = result
    result /= data ** 3
    result = result ** 10

    return result

answer = calculating_math_func(2)
print(answer)
answer = calculating_math_func(3)
print(answer)
answer = calculating_math_func(2)
print(answer)
