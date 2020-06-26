class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + str(birth_year)

first_name = input()
surname = input()
year = int(input())

new_student = Student(first_name, surname, year)
print(new_student.id)
