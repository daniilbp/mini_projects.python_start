import random


class Unit:
    def __init__(self, index):
        self.index = index
        self.name = 'Воин'
        self.halth = 100

    def print_info(self):
        print(self.name, f'{self.index}:', self.halth, 'здоровья.\n')

    def info_halth(self):
        if self.halth > 0:
            return True
        return False

class Units:
    def __init__(self):
        self.lst_units = [Unit(index) for index in range(1, 3)]

    def fight(self):
        while all([i_unit.info_halth() for i_unit in self.lst_units]):
            i_hited = random.randint(0, 1)
            i_rival = 1 - i_hited
            self.lst_units[i_rival].halth -= 20
            print(f'Атаковал {self.lst_units[i_hited].name} {self.lst_units[i_hited].index}')
            self.lst_units[i_rival].print_info()

        print(f'Победил {self.lst_units[i_hited].name} {self.lst_units[i_hited].index}')

my_units = Units()
my_units.fight()
