def do_dict_func(text):
    output_dict = {}
    for sym in text:
        if sym in output_dict:
            output_dict[sym] += 1
        else:
            output_dict[sym] = 1
    return output_dict

def count_func(input_dict):
    output_count = 0
    for info in input_dict:
        if input_dict[info] % 2 != 0:
            output_count += 1
    return output_count

def attempt_result(num):
    if num > 1:
        print('Нельзя сделать палиндромом')
    else:
        print('Можно сделать палиндромом')

user_text = input('Введите строку: ')

user_dict = do_dict_func(user_text)

num_count = count_func(user_dict)

attempt_result(num_count)


