import random


class Human:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def playing(self):
        print(f'{self.name} играет')
        self.satiety -= 1

    def is_satiety(self):
        if self.satiety <= 0:
            return False
        return True

class House:
    def __init__(self, count, food=50, money=0):
        self.food = food
        self.money = money
        self.humans = [Human(input(f'Имя {index} человека: ')) for index in range(1, count + 1)]

    def eating(self, human):
        print(f'{human.name} кушает.')
        human.satiety += 1
        self.food -= 1

    def working(self, human):
        print(f'{human.name} идет работать.')
        human.satiety -= 1
        self.money += 1

    def shopping(self, human):
        print(f'{human.name} идет в магазин за едой.')
        self.food += 1
        self.money -= 1

    def day_routine(self, human, day):
        num_cube = random.randint(1, 6)
        print(f'\nДень {day}. Число куба: {num_cube}.')
        # print(f' Что делает {human.name}:')
        if human.satiety < 20:
            self.eating(human)
        elif self.food < 10:
            self.shopping(human)
        elif self.money < 50:
            self.working(human)
        elif num_cube == 1:
            self.working(human)
        elif num_cube == 2:
            self.eating(human)
        else:
            human.playing()

    def print_info(self):
        print(f'\nЕда: {self.food}. Деньги: {self.money}\n', {el.name: el.satiety for el in self.humans})


my_house = House(2)

for day in range(1, 366):
    for i_human in my_house.humans:
        my_house.day_routine(i_human, day)
    my_house.print_info()
    if not all([my_house.humans[ind].is_satiety() for ind in range(2)]):
        print('Умер человек. Так дальше жить нельзя!')
        break
