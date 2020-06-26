camel_case = input()

for letter in camel_case:
    if letter.isupper():
        print('_' + letter.lower(), end='')
    else:
        print(letter, end='')
