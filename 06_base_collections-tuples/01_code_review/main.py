students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# v1
def students_info(input_dict):
    output_set = []
    output_len = 0

    for key, value in input_dict.items():

        output_set.extend(value['interests'])

        output_len += len(value['surname'])

    return set(output_set), output_len

pairs = [(key, value['age']) for key, value in students.items()]
print('Список пар "ID студента — возраст":', pairs)

interests, len_surname = students_info(students)

print('Полный список интересов всех студентов:', interests)
print('Общая длина всех фамилий студентов:', len_surname)

# v2
# pairs = [(key, value['age']) for key, value in students.items()]
# interes = set([el for key, value in students.items() for el in value['interests']])
# suren = len(''.join([value['surname'] for key, value in students.items()]))
#
# print('\nСписок пар "ID студента — возраст":', pairs)
# print('Полный список интересов всех студентов:', interes)
# print('Общая длина всех фамилий студентов:', suren)

# v3
# def students_info(input_dict):
#     output_list = []
#     output_set = []
#     output_len = 0
#
#     for key, value in input_dict.items():
#
#         output_list.append((key, value['age']))
#
#         output_set.extend(value['interests'])
#
#         output_len += len(value['surname'])
#
#     return output_list, set(output_set), output_len
#
# pairs_list, interests, len_surname = students_info(students)
#
# print('Список пар "ID студента — возраст":', pairs_list)
# print('Полный список интересов всех студентов:', interests)
# print('Общая длина всех фамилий студентов:', len_surname)