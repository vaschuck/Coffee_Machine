hour1 = int(input())
minute1 = int(input())
second1 = int(input())

hour2 = int(input())
minute2 = int(input())
second2 = int(input())

seconds = (hour2 - hour1) * 3600 + (minute2 - minute1) * 60 + (second2 - second1)
print(seconds)
