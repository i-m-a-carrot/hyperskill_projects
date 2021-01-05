class CoffeeMachine:
    def __init__(self, machine_repo,list_coffee):
            self.machine_repo = machine_repo
            self.list_coffee = list_coffee

    def display_remaining(self):
        print(f'''
The coffee machine has:
{self.machine_repo['water']} of water
{self.machine_repo['milk']} of milk
{self.machine_repo['coffee_beans']} of coffee beans
{self.machine_repo['dis_cups']} of disposable cups
${self.machine_repo['money']} of money
        ''')

    def perform_buy(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        buy_input = input()
        if buy_input.isnumeric():
            buy_input = int(buy_input)

            if self.machine_repo['water'] < 250:
                print('Sorry, not enough water!')
            elif self.machine_repo['milk'] < 50:
                print('Sorry, not enough milk')
            elif self.machine_repo['coffee_beans'] <15:
                print('Sorry, not enough beans of coffee')
            elif self.machine_repo['dis_cups'] < 1:
                print('Sorry, not enough cups')

            elif buy_input == 1:
                    self.machine_repo['water'] -= self.list_coffee['espresso']['water']
                    self.machine_repo['coffee_beans'] -= self.list_coffee['espresso']['coffee_beans']
                    self.machine_repo['dis_cups'] -= 1
                    self.machine_repo['money'] += self.list_coffee['espresso']['money']
                    print("I have enough resources, making you a coffee!")
            elif buy_input == 2:
                    self.machine_repo['water'] -= self.list_coffee['latte']['water']
                    self.machine_repo['milk'] -= self.list_coffee['latte']['milk']
                    self.machine_repo['coffee_beans'] -= self.list_coffee['latte']['coffee_beans']
                    self.machine_repo['dis_cups'] -= 1
                    self.machine_repo['money'] += self.list_coffee['latte']['money']
                    print("I have enough resources, making you a coffee!")
            elif buy_input == 3:
                    self.machine_repo['water'] -= self.list_coffee['cappuccino']['water']
                    self.machine_repo['milk'] -= self.list_coffee['cappuccino']['milk']
                    self.machine_repo['coffee_beans'] -= self.list_coffee['cappuccino']['coffee_beans']
                    self.machine_repo['dis_cups'] -= 1
                    self.machine_repo['money'] += self.list_coffee['cappuccino']['money']
            else:
                return
            print()

    def refill_machine_repo(self):
        print()
        print("Write how many ml of water do you want to add:")
        water_input = int(input())
        self.machine_repo['water'] += water_input
        print("Write how many ml of milk do you want to add:")
        milk_input = int(input())
        self.machine_repo['milk'] += milk_input
        print("Write how many grams of coffee beans do you want to add:")
        coffee_beans_input = int(input())
        self.machine_repo['coffee_beans'] += coffee_beans_input
        print("Write how many disposable cups of coffee do you want to add:")
        dis_cups_input = int(input())
        self.machine_repo['dis_cups'] += dis_cups_input
        print()

    def take_money(self):
        take_value = self.machine_repo['money']
        self.machine_repo['money'] -= take_value
        print(f"I gave you ${take_value}")
        print()
machine_repo = {"water": 400,"milk" : 540,"coffee_beans":120,"dis_cups":9,"money" : 550}

espresso = {"water":250,"coffee_beans":16,"money":4}
latte = {"water":350,"milk":75,"coffee_beans":20,"money":7}
cappuccino = {"water":200,"milk":100,"coffee_beans":12,"money":6}

list_coffee = {
    "espresso" : espresso,
    "latte" : latte,
    "cappuccino" : cappuccino
}
coffeeMachine = CoffeeMachine(machine_repo,list_coffee)

while True:
    print("Write action (buy, fill, take, remaining, exit): ")
    menu_input = input()
    if menu_input == "buy":
        coffeeMachine.perform_buy()
    elif menu_input == "fill":
        coffeeMachine.refill_machine_repo()
    elif menu_input == "remaining":
        coffeeMachine.display_remaining()
    elif menu_input == "take":
        coffeeMachine.take_money()
    elif menu_input == "exit":
        exit()

