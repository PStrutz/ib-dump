class CoffeeMachine:
    def __init__(self, water, milk, beans, disposable_cups, money):     
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money


    def display_status(self):       
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print(str(self.money) + " of money")

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - return to main menu:")
        choice = input()
        if choice.strip() == "1" and self.enough_resources("1"):
            self.water -= 250
            self.beans -= 16
            self.disposable_cups -= 1
            self.money += 4
        elif choice.strip() == "2" and self.enough_resources("2"):
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.disposable_cups -= 1
            self.money += 7
        elif choice.strip() == "3" and self.enough_resources("3") == True:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.disposable_cups -= 1
            self.money += 6
     
     
    def fill(self):
        print("Write how many ml of water do you want to add:")
        add_water = int(input())
        print("Write how many ml of milk do you want to add:")
        add_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        add_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        add_cups = int(input())
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.disposable_cups += add_cups

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def enough_resources(self, coffee_type):
        enough_water = True
        enough_milk = True
        enough_beans = True
        if self.disposable_cups < 1:
            print("Sorry, not enough cups!")
            return False
        else:
            if coffee_type == "1":
                if self.water < 250:
                    enough_water = False
                elif self.beans <= 16:
                    enough_beans = False
            elif coffee_type == "2":
                if self.water < 350:
                    enough_water = False
                elif self.milk < 75:
                    enough_milk = False
                elif self.beans < 20:
                    enough_beans = False
            elif coffee_type == "3":
                if self.water < 200:
                    enough_water = False
                elif self.milk < 100:
                    enough_milk = False
                elif self.beans < 12:
                    enough_beans = False
        
            if enough_water == False:
                print("Sorry, not enough water!")  
                return False
            elif enough_milk == False:
                print("Sorry, not enough milk!")
                return False
            elif enough_beans == False:
                print("Sorry, not enough beans!")
                return False
            else:
                print("I have enough resources, making you a coffee!")
                return True      
    


    def run(self):
        
        self.exit = False

        while self.exit == False:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()
            if action.strip() == "buy":
                self.buy()
            elif action.strip() == "fill":
                self.fill()
            elif action.strip() == "take":
                self.take()
            elif action.strip() == "remaining":
                self.display_status()
            elif action.strip() == "exit":
                self.exit = True

machine = CoffeeMachine(400, 540, 120, 9, 550)
machine.run()
