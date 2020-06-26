scores = input().split()

count_i = count_c = 0
for score in scores:
    if count_i == 3:
        print('Game over')
        break
    if score == 'C':
        count_c += 1
    else:
        count_i += 1
else:
    print('You won')

print(count_c)
