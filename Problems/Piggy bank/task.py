class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars

        total_cents = self.cents + deposit_cents
        if total_cents >= 100:
            self.cents = total_cents % 100
            self.dollars += total_cents // 100
        else:
            self.cents += deposit_cents



