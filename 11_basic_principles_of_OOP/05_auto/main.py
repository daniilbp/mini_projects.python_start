import math


class Car:
    def __init__(self, x=0, y=0, corner=90):
        self.x = x
        self.y = y
        self.corner = corner % 360

    def drive(self, distance):
        if -90 <= self.corner <= 90:
            rad_corner = self.corner * math.pi / 180
            self.y += math.sin(rad_corner) * distance
            self.x += math.cos(rad_corner) * distance
        elif -180 <= self.corner <= 180:
            rad_corner = (90 - self.corner % 90) * math.pi / 180
            self.y += math.sin(rad_corner) * distance
            self.x += -(math.cos(rad_corner) * distance)
        elif -270 <= self.corner <= 270:
            rad_corner = (self.corner % 90) * math.pi / 180
            self.y += -(math.sin(rad_corner) * distance)
            self.x += -(math.cos(rad_corner) * distance)
        else:
            rad_corner = (90 - self.corner % 90) * math.pi / 180
            self.y += -(math.sin(rad_corner) * distance)
            self.x += math.cos(rad_corner) * distance

    def turn(self, corner):
        self.corner = (self.corner + corner) % 360

    def __str__(self):
        return f'x: {round(self.x, 2)}\ty: {round(self.y, 2)}\tcorner: {self.corner}'


class Bus(Car):
    def __init__(self, x=0, y=0, corner=90, people=0, money=0):
        super().__init__(x, y, corner)
        self.people = people
        self.money = money
        self.price = 1

    def come_in(self, people):
        self.people += people

    def go_out(self, people):
        self.people -= people

    def drive(self, distance):
        super().drive(distance)
        self.money += self.people * distance * self.price

    def __str__(self):
        info = super().__str__()
        return f'{info}\nPeople: {self.people}\tMoney: {self.money}'


bus_1 = Bus()
bus_1.come_in(5)
bus_1.drive(1)
bus_1.go_out(3)
bus_1.turn(45)
bus_1.drive(math.sqrt(2))
print(bus_1)
