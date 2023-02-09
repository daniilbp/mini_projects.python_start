nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

answer_list = [el for second_list in nice_list for third_list in second_list for el in third_list]

print(answer_list)

# answer_list = []
# for second_list in nice_list:
#     for third_list in second_list:
#         for el in third_list:
#             answer_list.append(el)
#
# print(answer_list)