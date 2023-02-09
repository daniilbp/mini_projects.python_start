def slicer(input_tuple, sym):
    new_list = list(input_tuple)
    if new_list.count(sym) < 1:
        output_tuple = ()
    elif new_list.count(sym) == 1:
        output_tuple = tuple(new_list[new_list.index(sym):])
    else:
        first_ind_sym = new_list.index(sym)
        cut_list = new_list[first_ind_sym + 1:]
        second_ind_sym = cut_list.index(sym) + len(new_list[:first_ind_sym + 1])
        output_tuple = tuple(new_list[first_ind_sym:second_ind_sym + 1])

    return output_tuple

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
