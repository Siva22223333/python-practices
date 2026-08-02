class CoffeeMachine:
    def __init__(self):
        self.water_level = 100
        self.coffee_beans = 50

    def make_coffee(self):
        if self.water_level >= 20 and self.coffee_beans >= 10:
            print("Coffee is ready!")
            self.water_level -= 20
            self.coffee_beans -= 10
        else:
            print("Please refill.")

        print("Water:", self.water_level)
        print("Beans:", self.coffee_beans)

    def refill(self):
        self.water_level = 100
        self.coffee_beans = 50
        print("Machine refilled!")


machine = CoffeeMachine()

machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()
machine.make_coffee()   #

machine.refill()

machine.make_coffee()