CHICKEN = 23
GOAT = 678
PIG = 1296
COW = 3848
SHEEP = 6769

cash = int(input())

if cash >= SHEEP:
    sheep = cash // SHEEP
    print(sheep, 'sheep')
elif cash >= COW:
    cows = cash // COW
    print(cows, 'cow' if cows == 1 else 'cows')
elif cash >= PIG:
    pigs = cash // PIG
    print(pigs, 'pig' if pigs == 1 else 'pigs')
elif cash >= GOAT:
    goats = cash // GOAT
    print(goats, 'goat' if goats == 1 else 'goats')
elif cash >= CHICKEN:
    chickens = cash // CHICKEN
    print(chickens, 'chicken' if chickens == 1 else 'chickens')
else:
    print('None')
