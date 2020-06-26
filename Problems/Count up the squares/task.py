sum_ = sum_squares = 0

while True:
    number = int(input())
    sum_ += number
    sum_squares += (number ** 2)
    if sum_ == 0:
        break
print(sum_squares)
