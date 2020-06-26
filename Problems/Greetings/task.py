class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, I am {self.name}!')

name_person = input()

person = Person(name_person)
person.greet()
