numbers = []
while True:
    number = input()
    if number == '.':
        break
    numbers += [float(number)]

print(min(numbers))
