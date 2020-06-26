vowels = 'aeiou'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

letters = input()

for letter in letters:
    if letter not in alphabet:
        break
    if letter in vowels:
        print('vowel')
    else:
        print('consonant')
