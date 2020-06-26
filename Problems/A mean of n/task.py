lines = int(input())

sum_ = 0
for _ in range(lines):
    number = int(input())
    sum_ += number

average = sum_ / lines
print(average)
