class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    def calc_salary(self):
        pass

    def __str__(self):
        return f'{self.get_name()} {self.get_surname()}: {self.get_age()} y.o. Vacation: {self.__class__.__name__}\tSalary: {self.calc_salary()}'


class Manager(Employee):
    def calc_salary(self, salary=13000):
        self.salary = salary
        return self.salary


class Agent(Employee):
    def __init__(self, name, surname, age, sale_res):
        super().__init__(name, surname, age)
        self.percent = 5 * sale_res / 100

    def calc_salary(self):
        self.salary = 5000 * self.percent
        return self.salary


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def calc_salary(self):
        self.salary = 100 * self.hours
        return self.salary


manager_1 = Manager('Bob', 'Bobovsky', 35)
manager_2 = Manager('Caty', 'Powell', 30)
manager_3 = Manager('Roy', 'Adkinson', 25)
agent_1 = Agent('Chil', 'Thomson', 18, 100000)
agent_2 = Agent('Gill', 'Hugges', 48, 1000000)
agent_3 = Agent('Reese', 'Witherspoon', 58, 10000)
worker_1 = Worker('Glen', 'Foyd', 24, 40)
worker_2 = Worker('David', 'Backham', 29, 32)
worker_3 = Worker('Zizu', 'Zidan', 32, 48)

print(manager_1)
print(manager_2)
print(manager_3)
print(agent_1)
print(agent_2)
print(agent_3)
print(worker_1)
print(worker_2)
print(worker_3)
