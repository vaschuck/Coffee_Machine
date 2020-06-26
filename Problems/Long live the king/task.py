row = int(input())
col = int(input())

if row in (1, 8) and col in (1, 8):
    print(3)
elif row in (1, 8) or col in (1, 8):
    print(5)
else:
    print(8)
