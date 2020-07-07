class Coffee_machine:
    # main supplies
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    # main action
    def __init__(self):
        self.action()

    # actual action
    def action(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit): ')
            if action.lower() == 'buy':
                print('What do you want to buy? ',
                      '\n1 - espresso',
                      '\n2 - latte',
                      '\n3 - cappuccino',
                      '\nback - to main menu')
                self.buy_function(input())

            elif action.lower() == 'fill':
                self.fill_function()

            elif action.lower() == 'take':
                self.take_function()
            elif action.lower() == 'remaining':
                self.supplies()
            elif action.lower() == 'exit':
                return
            else:
                print("Sorry, coffee machine doesn't support "
                      "this function yet, choose another")

    # supplies
    def supplies(self):
        print('\nThe coffee machine has: \n',
              Coffee_machine.water, 'of water\n',
              Coffee_machine.milk, 'of milk\n',
              Coffee_machine.beans, 'of coffee beans\n',
              Coffee_machine.cups, 'of disposable cups\n',
              Coffee_machine.money, 'of money\n')

    # main functions for actions
    def buy_function(self, m):
        # espresso
        if m == '1':
            if Coffee_machine.water >= 250:
                if Coffee_machine.beans >= 16:
                    if Coffee_machine.cups >= 1:
                        print('I have enough resources, making you a coffee!')
                        Coffee_machine.water -= 250
                        Coffee_machine.beans -= 16
                        Coffee_machine.cups -= 1
                        Coffee_machine.money += 4
                    else:
                        print('Sorry, not enough cups!')
                else:
                    print('Sorry, not enough coffee beans!')
            else:
                print('Sorry, not enough water!')

        # latte
        elif m == '2':
            if Coffee_machine.water >= 350:
                if Coffee_machine.milk >= 75:
                    if Coffee_machine.beans >= 20:
                        if Coffee_machine.cups >= 1:
                            print('I have enough resources, making you a coffee!')
                            Coffee_machine.water -= 350
                            Coffee_machine.milk -= 75
                            Coffee_machine.beans -= 20
                            Coffee_machine.cups -= 1
                            Coffee_machine.money += 7
                        else:
                            print('Sorry, not enough cups!')
                    else:
                        print('Sorry, not enough coffee beans!')
                else:
                    print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough water!')
        # cappuccino
        elif m == '3':
            if Coffee_machine.water >= 200:
                if Coffee_machine.milk >= 100:
                    if Coffee_machine.beans >= 12:
                        if Coffee_machine.cups >= 1:
                            print('I have enough resources, making you a coffee!')
                            Coffee_machine.water -= 200
                            Coffee_machine.milk -= 100
                            Coffee_machine.beans -= 12
                            Coffee_machine.cups -= 1
                            Coffee_machine.money += 6
                        else:
                            print('Sorry, not enough cups!')
                    else:
                        print('Sorry, not enough coffee beans!')
                else:
                    print('Sorry, not enough milk!')
            else:
                print('Sorry, not enough water!')
        else:
            pass

    def fill_function(self):
        Coffee_machine.water += int(input('Write how many ml of water do you want to add: '))
        Coffee_machine.milk += int(input('Write how many ml of milk do you want to add: '))
        Coffee_machine.beans += int(input('Write how many grams of coffee beans do you want to add: '))
        Coffee_machine.cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take_function(self):
        print('I gave you $' + str(Coffee_machine.money))
        Coffee_machine.money = 0

act = Coffee_machine()


