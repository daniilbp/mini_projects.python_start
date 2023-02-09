class Property:
    def __init__(self, worth):
        self.worth = worth

    def tax_count(self):
        pass


class Apartment(Property):
    def tax_count(self):
        self.apart_tax = self.worth / 1000
        print(f'Стоимость {self.__class__.__name__}: {self.worth}\tНалог на квартиру: {self.apart_tax}')
        # return self.apart_tax


class Car(Property):
    def tax_count(self):
        self.car_tax = self.worth / 200
        print(f'Стоимость {self.__class__.__name__}: {self.worth}\tНалог на машину: {self.car_tax}')
        # return self.car_tax


class CountryHouse(Property):
    def tax_count(self):
        self.house_tax = self.worth / 500
        print(f'Стоимость {self.__class__.__name__}: {self.worth}\tНалог на дачу: {self.house_tax}')
        # return self.house_tax


def calc_tax():
    user_cash = int(input('Введите кол-во денег: '))
    # apart_price = int(input('Введите кол-во денег: '))
    # car_price = int(input('Введите кол-во денег: '))
    # house_price = int(input('Введите кол-во денег: '))

    apart = Apartment(int(input('Стоимость квартиры: ')))
    car = Car(int(input('Стоимость машины: ')))
    house = CountryHouse(int(input('Стоимость дачи: ')))

    apart.tax_count()
    car.tax_count()
    house.tax_count()

    all_tax = apart.apart_tax + car.car_tax + house.house_tax

    if all_tax <= user_cash:
        print('\nВсе ок, денег хватает, не потрать!')
    else:
        print(f'\nНе хватает {all_tax - user_cash}')


calc_tax()
