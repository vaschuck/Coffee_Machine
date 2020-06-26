WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15

print('Write how many ml of water the coffee machine has:')
water = int(input())
print('Write how many ml of milk the coffee machine has:')
milk = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input())
print('Write how many cups of coffee you will need:')
coffees = int(input())

cups_water = water // WATER_PER_CUP
cups_milk = milk // MILK_PER_CUP
cups_beans = beans // BEANS_PER_CUP

cups = min(cups_water, cups_milk, cups_beans)

if cups == coffees:
    print('Yes, I can make that amount of coffee')
elif cups > coffees:
    extra = cups - coffees
    print('Yes, I can make that amount of coffee',
          '(and even', extra, 'more than that)')
else:
    print('No, I can make only', cups, 'cups of coffee')
