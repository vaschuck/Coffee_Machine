min_sleep = int(input())
max_sleep = int(input())
sleep = int(input())

if min_sleep <= sleep <= max_sleep:
    print('Normal')
else:
    if min_sleep > sleep:
        print('Deficiency')
    else:
        print('Excess')
