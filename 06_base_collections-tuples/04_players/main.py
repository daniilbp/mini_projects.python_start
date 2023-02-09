players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# v.1
# final_list = []
#
# for key, values in players.items():
#     new_list = []
#     new_list.extend(list(key))
#     new_list.extend(list(values))
#     new_tuple = tuple(new_list)
#     final_list.append(new_tuple)

# v.2
print([key + values for key, values in players.items()])

# v.3
# print([sum((key, value), ()) for key, value in players.items()])

# v.4
# print(list(i_key + i_value for i_key, i_value in players.items()))
