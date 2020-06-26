class CoffeeMachine:
    def __init__(self):
        self.cash = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.state = 'Choosing option'

    def __str__(self):
        return f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.cash} of money'''

    def process_input(self, string):
        if self.state == 'Choosing option':
            if string == 'buy':
                self.state = 'Choosing coffee'
            elif string == 'fill':
                self.state = 'Filling machine water'
            elif string == 'take':
                self.take_money()
                print()
            elif string == 'remaining':
                print(self)
                print()
            else:
                self.state = 'Exiting'
        elif self.state == 'Choosing coffee':
            if string == '1':
                self.make_espresso()
                print()
            elif string == '2':
                self.make_latte()
                print()
            elif string == '3':
                self.make_cappuccino()
                print()
            self.state = 'Choosing option'
        elif self.state == 'Filling machine water':
            self.fill_water(int(string))
            self.state = 'Filling machine milk'
        elif self.state == 'Filling machine milk':
            self.fill_milk(int(string))
            self.state = 'Filling machine beans'
        elif self.state == 'Filling machine beans':
            self.fill_beans(int(string))
            self.state = 'Filling machine cups'
        elif self.state == 'Filling machine cups':
            self.fill_cups(int(string))
            self.state = 'Choosing option'
            print()

    def make_espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.cash += 4
        else:
            if 250 > self.water:
                print('Sorry, not enough water!')
            if 16 > self.beans:
                print('Sorry, not enough beans!')
            if 1 > self.cups:
                print('Sorry not enough cups!')

    def make_latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.cash += 7
        else:
            if 350 > self.water:
                print('Sorry, not enough water!')
            if 75 > self.milk:
                print('Sorry, not enough milk!')
            if 20 > self.beans:
                print('Sorry, not enough beans!')
            if 1 > self.cups:
                print('Sorry not enough cups!')

    def make_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.cash += 6
        else:
            if 200 > self.water:
                print('Sorry, not enough water!')
            if 100 > self.milk:
                print('Sorry, not enough milk!')
            if 12 > self.beans:
                print('Sorry, not enough beans!')
            if 1 > self.cups:
                print('Sorry not enough cups!')

    def fill_water(self, param):
        self.water += param

    def fill_milk(self, param):
        self.milk += param

    def fill_beans(self, param):
        self.beans += param

    def fill_cups(self, param):
        self.cups += param

    def take_money(self):
        print('I gave you $' + str(self.cash))
        self.cash = 0


def main():
    coffee_machine = CoffeeMachine()
    while coffee_machine.state != 'Exiting':
        if coffee_machine.state == 'Choosing option':
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            print()
            coffee_machine.process_input(action)
        elif coffee_machine.state == 'Choosing coffee':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            choice = input()
            coffee_machine.process_input(choice)
        elif coffee_machine.state == 'Filling machine water':
            print('Write how many ml of water do you want to add:')
            water_ = input()
            coffee_machine.process_input(water_)
        elif coffee_machine.state == 'Filling machine milk':
            print('Write how many ml of milk do you want to add:')
            milk_ = input()
            coffee_machine.process_input(milk_)
        elif coffee_machine.state == 'Filling machine beans':
            print('Write how many grams of coffee beans do you want to add:')
            beans_ = input()
            coffee_machine.process_input(beans_)
        elif coffee_machine.state == 'Filling machine cups':
            print('Write how many disposable cups of coffee do you want to add:')
            cups_ = input()
            coffee_machine.process_input(cups_)


main()
