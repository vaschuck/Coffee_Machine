list_numbers = []

while True:
    number_str = input()
    if number_str == '.':
        break
    number = int(number_str)
    list_numbers += [number]

print(sum(list_numbers) / len(list_numbers))
