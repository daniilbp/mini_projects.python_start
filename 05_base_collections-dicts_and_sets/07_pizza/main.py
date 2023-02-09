num_orders = int(input('Введите количество заказов: '))

orders_list = [input('{0}-й заказ: '.format(num)).split() for num in range(1, num_orders + 1)]

orders_dict = {}
for i_order in range(len(orders_list)):

    if orders_list[i_order][0] in orders_dict:
        if orders_list[i_order][1] in orders_dict[orders_list[i_order][0]]:
            orders_dict[orders_list[i_order][0]][orders_list[i_order][1]] += int(orders_list[i_order][2])
        else:
            orders_dict[orders_list[i_order][0]][orders_list[i_order][1]] = int(orders_list[i_order][2])

    else:
        orders_dict[orders_list[i_order][0]] = {orders_list[i_order][1]: int(orders_list[i_order][2])}

print()
for info in sorted(orders_dict.keys()):
    print(info + ':')
    for info_2 in sorted(orders_dict[info].keys()):
        print('    ', info_2 + ':', orders_dict[info][info_2])
