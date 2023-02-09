def generator(*args):

    min_len = min(len(el) for el in args)

    # zip_lst = [tuple(el[i] for el in map(list, args)) for i in range(min_len)]
    zip_lst = [tuple(el_2 for el in args for ind, el_2 in enumerate(el) if ind == i) for i in range(min_len)]

    print(zip_lst)

# generator('abcd', (10, 20, 30, 40))
generator('abcd', {1: 123, 2: 456, 3: 789, 4: 321})
