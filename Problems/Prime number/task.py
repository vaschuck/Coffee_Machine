number = int(input())

divisor = 2
is_prime = False

while divisor < number:
    if number % divisor == 0:
        break
    divisor += 1
else:
    if number != 1:
        is_prime = True

print('This number is prime' if is_prime else 'This number is not prime')
