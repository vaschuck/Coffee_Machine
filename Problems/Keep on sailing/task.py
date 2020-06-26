# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, place):
        print("The {} has sailed for {}!".format(self.name, place))


black_pearl = Ship("Black Pearl", 800)
location = input()
black_pearl.sail(location)
