def do_lst_1_lvl(lst):
    new_lst = []
    for el in lst:
        if isinstance(el, list):
            new_lst.extend(do_lst_1_lvl(el))
        else:
            new_lst.append(el)

    return new_lst

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(do_lst_1_lvl(nice_list))
