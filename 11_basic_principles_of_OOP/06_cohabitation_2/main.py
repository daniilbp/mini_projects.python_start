class FamilyMember:
    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety

    def check(self):
        if self.satiety <= 0:
            return False
        return True


class Human(FamilyMember):
    def __init__(self, name, satiety=30, happy=100):
        super().__init__(name, satiety)
        self.happy = happy

    def check(self):
        if super().check():
            if self.happy < 10:
                return False
            return True


class Cat(FamilyMember):
    pass


class House:
    def __init__(self, count_cat=3, food=50, money=100, cat_food=30, dirt=0, c_m=0, c_c=0, c_f=0, c_c_f=0):
        self.food = food
        self.cat_food = cat_food
        self.money = money
        self.dirt = dirt
        self.cat = [Cat(name_aka_Elon) for name_aka_Elon in range(1, count_cat+1)]
        self.husband = Human('Гена')
        self.wife = Human('Галя')
        self.child = Human('Гоша')
        self.count_money = c_m
        self.count_coat = c_c
        self.count_food = c_f
        self.count_cat_food = c_c_f
        self.family = [self.husband, self.wife, self.child]

    def eating(self, member):
        print(f'{member.name} кушает.')
        if isinstance(member, Human):
            if self.food >= 30:
                lvl_food = 30
            else:
                lvl_food = self.food
            self.food -= lvl_food
            self.count_food += lvl_food
            member.satiety += lvl_food
        else:
            if self.cat_food >= 10:
                lvl_food = 10
            else:
                lvl_food = self.food
            self.cat_food -= lvl_food
            self.count_cat_food += lvl_food
            member.satiety += (2 * lvl_food)

    def playing(self, member):
        print(f'{member.name} играет')
        if member == self.child:
            self.dirt -= 5
        member.satiety -= 10
        member.happy += 20

    def working(self):
        print(f'{self.husband.name} идет работать.')
        self.husband.satiety -= 10
        self.money += 150
        self.count_money += 150

    def buy_food(self):                 # Wife
        print('Жена покупает продукты.')
        self.food += 80
        self.money -= 80
        self.wife.satiety -= 10

    def buy_cat_food(self):
        print('Жена покупает корм коту.')
        self.cat_food += 80
        self.money -= 80
        self.wife.satiety -= 10

    def shopping(self):
        print('Жена идет за шубой.')
        self.money -= 350
        self.count_coat += 1
        self.wife.satiety -= 10
        self.wife.happy += 60

    def cleaning(self):
        print('Жена убирается.')
        if self.dirt >= 100:
            self.dirt -= 100
        else:
            self.dirt = 0
        self.wife.satiety -= 10

    def tear_wallpaper(self, cat):          # Cat
        print(f'{cat.name} дерет обои.')
        self.dirt += 5
        cat.satiety -= 10

    def sleep(self, member):
        print(f'{member.name} спит')
        member.satiety -= 10

    def pet_the_cat(self, member):
        print(f'{member.name} гладит котов')
        member.happy += 5
        member.satiety -= 10

    def day_routine(self, member, day):
        if isinstance(member, Human):
            if my_house.dirt > 90:
                member.happy -= 10
            if member.satiety < 20:
                self.eating(member)
            elif self.money < 300 and member == self.husband:
                self.working()
            elif self.food < 30 and member == self.wife:
                self.buy_food()
            elif self.cat_food < 40 and member == self.wife:
                self.buy_cat_food()
            elif member.happy < 30:
                if member == self.husband or member == self.child:
                    self.playing(member)
                elif member == self.wife and self.money >= 150:
                    self.shopping()
            elif self.dirt >= 90 and member == self.wife:
                self.cleaning()
            elif self.child == member:
                self.sleep(member)
            else:
                self.pet_the_cat(member)
        else:
            if member.satiety < 30:
                self.eating(member)
            elif self.dirt < 20:
                self.tear_wallpaper(member)
            else:
                self.sleep(member)

    def print_info(self):
        print(f'Еда: {self.food}. Корм для кота: {self.cat_food}. Деньги: {self.money}. Грязь: {self.dirt}\n',
              {member.name: f'Сытость: {member.satiety}. Счастья: {member.happy}' for member in self.family},
              '\n', {cat.name: cat.satiety for cat in self.cat}, '\n')


my_house = House()

for day in range(1, 366):
    print(f'День {day}.', end=' ')
    my_house.dirt += 5
    for i_human in my_house.family:
        my_house.day_routine(i_human, day)
    for i_cat in my_house.cat:
        my_house.day_routine(i_cat, day)
    my_house.print_info()
    if not all([my_house.family[ind].check() for ind in range(len(my_house.family))]):
        print('Умер член семьи. Так дальше жить нельзя!')
        break
    elif not all([my_house.cat[ind].check() for ind in range(3)]):
        print('Умер кот. Так дальше жить нельзя!')
        break

print(f'Итоги за год: Денег заработано: {my_house.count_money}. Еды съедено: {my_house.count_food}. '
      f'Корма съедено: {my_house.count_cat_food}. Шуб куплено: {my_house.count_coat}')
