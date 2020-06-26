number1 = int(input())
number2 = int(input())

count = 0
sum_ = 0
for number in range(number1, number2 + 1):
    if number % 3 == 0:
        sum_ += number
        count += 1

average = sum_ / count
print(average)
