cash = 550
water = 400
milk = 540
beans = 120
cups = 9


def display_status():
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    print('$', cash, ' of money', sep='')


def take_money():
    global cash
    print('I gave you $' + str(cash))
    cash = 0


def make_espresso():
    global water, beans, cups, cash
    if water >= 250 and beans >= 16 and cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 250
        beans -= 16
        cups -= 1
        cash += 4
    else:
        if 250 > water:
            print('Sorry, not enough water!')
        if 16 > beans:
            print('Sorry, not enough beans!')
        if 1 > cups:
            print('Sorry not enough cups!')


def make_latte():
    global water, milk, beans, cups, cash
    if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        cash += 7
    else:
        if 350 > water:
            print('Sorry, not enough water!')
        if 75 > milk:
            print('Sorry, not enough milk!')
        if 20 > beans:
            print('Sorry, not enough beans!')
        if 1 > cups:
            print('Sorry not enough cups!')


def make_cappuccino():
    global water, milk, beans, cups, cash
    if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
        print('I have enough resources, making you a coffee!')
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        cash += 6
    else:
        if 200 > water:
            print('Sorry, not enough water!')
        if 100 > milk:
            print('Sorry, not enough milk!')
        if 12 > beans:
            print('Sorry, not enough beans!')
        if 1 > cups:
            print('Sorry not enough cups!')


def buy_coffee():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    choice = input()
    if choice == '1':
        make_espresso()
    elif choice == '2':
        make_latte()
    elif choice == '3':
        make_cappuccino()


def fill_machine():
    global water, milk, beans, cups
    print('Write how many ml of water do you want to add:')
    added_water = int(input())

    print('Write how many ml of milk do you want to add:')
    added_milk = int(input())

    print('Write how many grams of coffee beans do you want to add:')
    added_beans = int(input())

    print('Write how many disposable cups of coffee do you want to add:')
    added_cups = int(input())

    water += added_water
    milk += added_milk
    beans += added_beans
    cups += added_cups


def main():
    while True:
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
        print()
        if action == 'buy':
            buy_coffee()
        elif action == 'fill':
            fill_machine()
        elif action == 'take':
            take_money()
        elif action == 'remaining':
            display_status()
        else:
            break
        print()
main()
