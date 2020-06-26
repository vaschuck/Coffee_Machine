digits = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

numbers_str = input()

for number_str in numbers_str:
    index = int(number_str)
    print(digits[index])
