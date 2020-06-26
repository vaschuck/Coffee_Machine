list_names = []
while True:
    name = input()
    if name == '.':
        break
    list_names += [name]

print(list_names)
print(len(list_names))
