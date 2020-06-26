lines = int(input())

for _ in range(lines):
    number = int(input())
    if number % 7 == 0:
        print(number ** 2)
