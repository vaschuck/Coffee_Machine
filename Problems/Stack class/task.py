class Stack():

    def __init__(self):
        self.elements = []

    def push(self, el):
        self.elements.append(el)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0
