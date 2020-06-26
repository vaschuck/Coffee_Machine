UTC_HOUR = 10

offset = int(input())

hour = UTC_HOUR + offset

if hour < 0:
    print('Monday')
elif hour >= 24:
    print('Wednesday')
else:
    print('Tuesday')
