days = int(input())
food_cost = int(input())
flight_cost = int(input())
night_cost = int(input())

total_cost = food_cost * days + night_cost * (days - 1) + flight_cost * 2
print(total_cost)
