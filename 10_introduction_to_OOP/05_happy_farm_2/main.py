class Potato:
    states = {0: 'Нет', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def print_state(self):
        print(f'Картошка {self.index} сейчвс {self.states[self.state]}')

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('\nВся картошка созрела. Можно собирать!\n')
            return True


class Gardener:
    def __init__(self, name, count):
        self.name = 'Gardenman'
        self.garden = PotatoGarden(count)

    def care(self, man):
        while not self.garden.all_ripe():
            self.garden.grow_all()
            # self.garden.all_ripe()
        man.ingathering()

    def ingathering(self, count_potatoes=0):
        for i_potato in self.garden.potatoes:
            if i_potato.is_ripe():
                count_potatoes += 1
                print(f'Собираем {i_potato.index} картошку.')
        print(f'Всего собрано: {count_potatoes} картошек')


gardener_1 = Gardener('Diaz', 5)
gardener_1.care(gardener_1)
