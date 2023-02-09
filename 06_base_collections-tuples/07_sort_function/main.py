def tpl_sort(num_1, num_2, num_3, num_4, num_5, num_6, num_7):
    input_tuple = (num_1, num_2, num_3, num_4, num_5, num_6, num_7)
    if sum(input_tuple) % 1 != 0:
        sort_tuple = input_tuple
    else:
        sort_tuple = sorted(input_tuple)

    return sort_tuple

print(tpl_sort(6, 3, -1, 8, 4, 1, -5))
