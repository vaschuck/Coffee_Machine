HALF_LIFE = 12

initial_quantity = int(input())
final_quantity = int(input())

half_lives = 0
while initial_quantity > final_quantity:
    initial_quantity //= 2
    half_lives += 1

print(half_lives * HALF_LIFE)
