''' contains the class definition of a Python Stack using Python Lists'''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self): # no need to put in a parameter
        return self.items.pop() # always want to remove from end (top element)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
