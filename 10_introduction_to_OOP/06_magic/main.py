class Water:
    name = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    name = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    name = 'Земля'
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None


class Storm:
    name = 'Щторм'
    answer = 'Вода + Воздух = Шторм'
    def __add__(self, other):
        return None


class Steam:
    name = 'Пар'
    answer = 'Вода + Огонь = Пар'
    def __add__(self, other):
        return None


class Dirt:
    name = 'Грязь'
    answer = 'Вода + Земля = Грязь'
    def __add__(self, other):
        return None


class Lightning:
    name = 'Молния'
    answer = 'Воздух + Огонь = Молния'
    def __add__(self, other):
        return None


class Dust:
    name = 'Пыль'
    answer = 'Воздух + Земля = Пыль'
    def __add__(self, other):
        return None


class Lava:
    name = 'Лава'
    answer = 'Огонь + Земля = Лава'
    def __add__(self, other):
        return None


el_1 = Water()
el_2 = Air()
el_3 = Fire()
el_4 = Earth()

el_5 = el_1 + el_2
print(el_5.name)
el_6 = el_1 + el_3
print(el_6.name)
el_7 = el_1 + el_4
print(el_7.name)
el_8 = el_2 + el_3
print(el_8.name)
el_9 = el_2 + el_4
print(el_9.name)
el_10 = el_3 + el_4
print(el_10.name)
el_11 = el_1 + el_5
print(el_11)
