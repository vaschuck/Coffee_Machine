deposit = int(input())
years = 0

while deposit < 700000:
    interest = deposit * 0.071
    deposit += interest
    years += 1
print(years)
