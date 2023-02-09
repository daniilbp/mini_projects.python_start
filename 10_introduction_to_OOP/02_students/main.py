import random

class Student:
    def __init__(self, index):
        self.name = f'Студент №{index}'
        self.group = random.randint(1, 3)
        self.progress = [random.randint(0, 5) for _ in range(5)]

    def print_info(self):
        print(self.name, self.group, self.progress)

    def middle_progress(self):
        return sum(self.progress) / len(self.progress)

students = [Student(index) for index in range(1, 11)]

lst_middle_progress = [students[i].middle_progress() for i in range(10)]

dct_students = {students[i]: lst_middle_progress[i] for i in range(10)}

sort_lst_middle_progress = sorted(lst_middle_progress)

sort_students = []
for el in sort_lst_middle_progress:
    for key, value in dct_students.items():
        if el == value and key not in sort_students:
            sort_students.append(key)

for i in range(10):
    sort_students[i].print_info()
