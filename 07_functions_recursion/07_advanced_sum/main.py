def do_sum(*args):

    def do_sum_2(lst):
        return sum([do_sum_2(el_lst) if isinstance(el_lst, list) else el_lst for el_lst in lst])

    print(sum([do_sum_2(el) if isinstance(el, list) else el for el in args]))


do_sum(1, 2, 3, 4, 5)

# do_sum([[1, 2, [3]], [1], 3])
