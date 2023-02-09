import random


class KillError(Exception):
    def __str__(self):
        return 'Случайно умер.'


class DrunkError(Exception):
    def __str__(self):
        return 'ПерепИл.'


class CarCrashError(Exception):
    def __str__(self):
        return 'Сбил автобус.'


class GluttonyError(Exception):
    def __str__(self):
        return 'Перекушал.'


class DepressionError(Exception):
    def __str__(self):
        return 'Сегодня грусть, тоска...'


class Karma:
    __target_karma = 500
    __count = 0
    def __init__(self):
        Karma.__count += 1
        if self.one_day():
            Karma.__target_karma -= self.karma
            print(f'День {self.__count}: Карма дня: {self.karma}\tДо просветления: {self.__target_karma} кармы.')

    def get_karma(self):
        return self.__target_karma

    def get_count(self):
        return self.__count

    def one_day(self):
        with open('karma.txt', 'a', encoding='utf-8') as file:
            random_exception = random.randint(1, 10)
            try:
                if random_exception == 1:
                    lst_exception = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
                    ind_exception = random.randint(0, len(lst_exception)-1)
                    raise lst_exception[ind_exception]
                else:
                    self.karma = random.randint(1, 7)
                    return self.karma
            except lst_exception[ind_exception]:
                print(f'День {self.__count}:', lst_exception[ind_exception]())
                file.write(f'День {self.__count}: типа ошибки: {lst_exception[ind_exception]} - {lst_exception[ind_exception]()}\n')


def life_simulator():
    while True:
        day = Karma()
        # day.one_day()
        # print(day)

        res = day.get_karma()
        if res <= 0:
            break

    print(f'\nПоздравляю. Просветление достигнуто за {day.get_count()} дней!')


life_simulator()
