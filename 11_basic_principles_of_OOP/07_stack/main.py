import my_stack


class TaskManager:
    def __init__(self):
        self.stack = my_stack.Stack()
        self.dct = {}

    def __str__(self):
        info = ''
        for key in sorted(self.dct.keys()):
            info += str(key) + ' '
            for values in self.dct[key]:
                info += f'{values}; '
            info += '\n'
        return info

    def new_task(self, task, priority):
        try:
            if [task, priority] in self.stack.lst:
                raise KeyError
            else:
                if priority in self.dct:
                    self.dct[priority].append(task)
                else:
                    self.dct[priority] = [task]

                self.stack.append(task, priority)
        except KeyError:
            print('Дубликат, сперва закройте предыдущую задачу.')

    def delete_task(self, task, priority):
        if [task, priority] in self.stack.lst:
            self.stack.remove(task, priority)
            self.dct = {}
            for el in self.stack.lst:
                if el[1] in self.dct:
                    self.dct[el[1]].append(el[0])
                else:
                    self.dct[el[1]] = [el[0]]


manager = TaskManager()
manager.new_task('сделать уборку', 4)
manager.new_task('помыть посуду', 4)
manager.new_task('отдохнуть', 1)
manager.new_task('поесть', 2)
manager.new_task('сдать дз', 2)
print(manager)

manager.delete_task('поесть', 2)
print(manager)
