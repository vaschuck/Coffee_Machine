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
    print(cash, 'of money')


def take_money():
    global cash
    print('I gave you $' + str(cash))
    cash = 0


def make_espresso():
    global water, beans, cups, cash
    water -= 250
    beans -= 16
    cups -= 1
    cash += 4


def make_latte():
    global water, milk, beans, cups, cash
    water -= 350
    milk -= 75
    beans -= 20
    cups -= 1
    cash += 7


def make_cappuccino():
    global water, milk, beans, cups, cash
    water -= 200
    milk -= 100
    beans -= 12
    cups -= 1
    cash += 6


def buy_coffee():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    choice = int(input())

    if choice == 1:
        make_espresso()
    elif choice == 2:
        make_latte()
    elif choice == 3:
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
    display_status()
    print()

    print('Write action (buy, fill, take):')
    action = input()

    if action == 'buy':
        buy_coffee()
    elif action == 'fill':
        fill_machine()
    elif action == 'take':
        take_money()

    print()
    display_status()

main()
