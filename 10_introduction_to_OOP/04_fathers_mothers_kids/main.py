import random


class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = [Child(name, self.age) for name in children]

    def print_info(self):
        print(f'\nName: {self.name}\nAge: {self.age}\n'
              f'Children: {[{i_child.name: (i_child.age, i_child.state_of_calm, i_child.state_of_hunger)} for i_child in self.children]}\n')

    def calm(self, state_baby):
        if state_baby >= 7:
            print('Soothe the child.')
            state_baby -= 1
            return state_baby

    def eating(self):
        print('We feed the child')
        return 1

class Child:
    def __init__(self, name, parent_age, state_of_calm=None, state_of_hunger=None):
        self.name = name

        age = int(input(f'Age {self.name}: '))
        while True:
            try:
                if age + 16 > parent_age:
                    raise ValueError
                self.age = age
                break
            except ValueError:
                print('\nВозраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет')
                age = int(input(f'Age {self.name}: '))

        self.state_of_calm = state_of_calm
        self.state_of_hunger = state_of_hunger

    def new_calm(self):
        self.state_of_calm = random.randint(1, 10)
        while self.state_of_calm >= 7:
            print(f'State of calm: {self.state_of_calm}')
            self.state_of_calm = parent_1.calm(self.state_of_calm)
        print(f'Child is calm({self.state_of_calm})\n')

    def new_state_of_hungry(self):
        self.state_of_hunger = random.randint(0, 1)
        while self.state_of_hunger != 1:
            if self.age < 3:
                print('У-а-а-а-а-а. Ам-ам')
            else:
                print('Хочу кушать!')
            self.state_of_hunger = parent_1.eating()
        print('Child is fed.')

parent_1 = Parent('Bob', 30, ['Ann', 'Reese'])
parent_1.print_info()
parent_1.children[0].new_calm()
parent_1.children[1].new_state_of_hungry()
