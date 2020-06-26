num1 = float(input())
num2 = float(input())
operator = input()

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == 'pow':
    print(num1 ** num2)
elif num2 == 0:
    print('Division by 0!')
elif operator == '/':
    print(num1 / num2)
elif operator == 'mod':
    print(num1 % num2)
else:
    print(num1 // num2)
