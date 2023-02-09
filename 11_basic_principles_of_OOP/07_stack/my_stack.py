class Stack:
    def __init__(self):
        self.lst = []

    def append(self, task, priority):
        self.lst.append([task, priority])

    def extend(self, task, priority):
        self.lst.extend([task, priority])

    def remove(self, task, priority):
        while [task, priority] in self.lst:
            self.lst.remove(self.lst[len(self.lst) - 1])
