from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Базовый класс - фигуры
    Args и attrs:
        length (float): длина(основание) фигуры
        width (float): высота фигуры
     """
    def __init__(self, length: float, width: float) -> None:
        self._length = length
        self._width = width

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float) -> None:
        self._length = length


class MathMixin:
    """ Класс примеси для вычисление математики """
    def perimetr(self) -> float:
        return self._length * 2 + self._width * 2

    def area(self) -> float:
        return self._length * self._width

    @abstractmethod
    def surface_area(self) -> None:
        pass


class Square(Figure, MathMixin):
    """ Квадрат. Родительский класс Figure """
    def __init__(self, size: float) -> None:
        super().__init__(size, size)


class Triangle(Figure, MathMixin):
    """ Треугольник. Родительский класс Figure """
    def perimetr(self) -> float:
        res = super().perimetr()
        return res / 2

    def area(self) -> float:
        res = super().area()
        return res / 2


class Cube(Square):
    """ Куб. Родительский класс Square """
    def __init__(self, size: float) -> None:
        super().__init__(size)
        self.cube = [Square(size) for _ in range(6)]

    # def surface_area(self) -> float:
    #     return self.area() * 6

    def surface_area(self) -> float:
        return sum([i_el.area() for i_el in self.cube])


class Pyramid(Triangle):
    """ Пирамида. Родительский класс Triangle """
    def __init__(self, length: float, width: float) -> None:
        super().__init__(length, width)
        self.pyramid_1 = [Triangle(length, width) for _ in range(4)]
        self.pyramid_2 = [Square(length)]
        self.pyramid = self.pyramid_1 + self.pyramid_2

    # def surface_area(self) -> float:
    #     return self.area() * 4 + self.area() * 2

    def surface_area(self) -> float:
        return sum([i_el.area() for i_el in self.pyramid])


my_square = Square(2)
print(my_square.perimetr())
print(my_square.area())

my_triangle = Triangle(2, 2)
print(my_triangle.perimetr())
print(my_triangle.area())

my_cube = Cube(2)
print(my_cube.perimetr())
print(my_cube.area())
print(my_cube.surface_area())

my_pyramid = Pyramid(2, 2)
print(my_pyramid.perimetr())
print(my_pyramid.area())
print(my_pyramid.surface_area())
