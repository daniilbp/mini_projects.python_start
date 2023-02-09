import math


class Round:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def new_size(self, k):
        self.r = self.r * k

    def intersections(self, other_round):
        if self.r + other_round.r >= math.sqrt((self.x - other_round.x) ** 2 + (self.y - other_round.y) ** 2):
            print('Пересекаются')
        else:
            print('Не пересекаются')

round_1 = Round()
round_2 = Round(1, 1)

print(round_1.square())
print(round_1.perimeter())
round_1.intersections(round_2)
round_1.new_size(2)
print(round_1.x, round_1.y, round_1.r)
print(round_2.perimeter())
print(round_1.perimeter())
