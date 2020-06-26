WATER_PER_CUP = 200
MILK_PER_CUP = 50
BEANS_PER_CUP = 15

print('Write how many cups of coffee you will need:')
coffees = int(input())

water = coffees * WATER_PER_CUP
milk = coffees * MILK_PER_CUP
beans = coffees * BEANS_PER_CUP
print(water, 'ml of water')
print(milk, 'ml of milk')
print(beans, 'g of coffee beans')
