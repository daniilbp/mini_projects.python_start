from typing import Any, Optional


class Node:
    """
    Класс для создания нового узла.
    Args:
        value(Optional[Any]): передает значение узла
        next(Optional['Node']: передает ссылку на следующий узел
    """
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f'Node [{self.value}]'


class LinkedList:
    """
    Класс создающий связный список
    Attributes:
        self.head(Optional[Node]): голова списка
        self.length(int): счетчик длины для проверки индекса
    """
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 1

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{values}]'.format(values=' '.join(values))
        return 'LinkedList []'

    def append(self, num: Any) -> None:
        """
        Функция для создания: первого элемента в список или ссылки на следующий узел.
        :param num: значение элемента передоваемого в список
        :return: выход из функции, если создается первый узел
        """
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.length += 1

    def remove(self, index: int) -> None:
        """
        Функция для переопределения ссылки на следующий узел или переопределения головы списка, если удаляется 1ый элемент списка.
        :param index: значения индекса, который необходимо удалить
        :return: выход из функции, если переопределяется голова списка
        :raise IndexError: если индекс 0 или более длины
        """
        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError

        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1

        prev.next = cur_node.next
        self.length -= 1

    def get(self, ind: int) -> Any:
        """
        Функция для получения значения узла(элемента) по индексу.
        :param ind: индекс узла(элемента) списка, значение которого необходимо вывести на экран.
        :return: cur_node.value: значение узла при совпадении индексов
        :raise IndexError: если индекс 0 или более длины
        """
        cur_node = self.head
        cur_ind = 0
        if self.length == 0 or self.length <= ind:
            raise IndexError

        while cur_node is not None:
            if cur_ind == ind:
                return cur_node.value
            cur_node = cur_node.next
            cur_ind += 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
