import random
import sqlite3


class Simple_bank:
    account_exit = False
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS card  (id INTEGER,'
                'number TEXT,'
                'pin TEXT,'
                'balance INTEGER DEFAULT 0)'
                )
    conn.commit()

    def __init__(self):
        self.action()

    def luhn_check(self, card_number):
        last_digit = card_number[-1]
        converting = [i for i in card_number]
        # lists with conditions
        converting = [str(int(converting[i]) * 2) if i % 2 == 0 else converting[i] for i in range(15)]
        converting = [int(converting[i]) - 9 if int(converting[i]) > 9 else int(converting[i]) for i in range(15)]
        # last number
        i = 0
        while True:
            if (sum(converting) + i) % 10 == 0:
                if str(i) == last_digit:
                    return True
                else:
                    return False
            i += 1

    def luhn_create(self, unfinished_bin):
        unfinished_bin = '400000' + unfinished_bin
        # making a list
        converting = [i for i in unfinished_bin]
        # lists with conditions
        converting = [str(int(converting[i]) * 2) if i % 2 == 0 else converting[i] for i in range(15)]
        converting = [int(converting[i]) - 9 if int(converting[i]) > 9 else int(converting[i]) for i in range(15)]
        # last number
        i = 0
        while True:
            if (sum(converting) + i) % 10 == 0:
                unfinished_bin += str(i)
                break
            i += 1
        return unfinished_bin

    def new_account(self):
        while True:
            a = ''.join([str(random.randint(0, 9)) for i in range(9)])
            # 1st tuple- unchangeable => safer, 2nd i do check if table already had such card number
            a = self.luhn_create(a)
            check = (a,)
            Simple_bank.cur.execute('SELECT * FROM card WHERE number=?', check)
            if len(Simple_bank.cur.fetchall()):
                pass
            else:
                # 3rd, due to immutability i had to create different tuples
                acc = (a, ''.join([str(random.randint(0, 9)) for i in range(4)]))
                Simple_bank.cur.execute('INSERT INTO card (number, pin) VALUES (?, ?)', acc)
                print(f'''
Your card has been created
Your card number:
{acc[0]}
Your card PIN:
{acc[1]}
''')
                Simple_bank.conn.commit()
                break

    def login(self, card_number, pin):
        # tuple is good thing there, it's unchangeable and allows you to have several arguments
        attempt = (card_number, pin)
        Simple_bank.cur.execute('SELECT * FROM card WHERE number=? AND pin=?', attempt)
        if len(Simple_bank.cur.fetchall()):
            print('\nYou have successfully logged in!\n')
            self.acc_menu(card_number)
        else:
            print('\nWrong card number or PIN!\n')

    def acc_menu(self, card_number):
        while True:
            print("""\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
            account_act = input()

            if account_act == '1':
                check = (card_number,)
                Simple_bank.cur.execute('SELECT balance FROM card WHERE number=?', check)
                # fetchall output is list and insides are tuples
                print(f'\nBalance: {Simple_bank.cur.fetchall()[0][0]}')

            elif account_act == '2':
                income = int(input('\nEnter income: '))
                change = (income, card_number)
                Simple_bank.cur.execute('UPDATE card SET balance = balance + ? WHERE number=?', change)
                Simple_bank.conn.commit()
                print('\nIncome was added!\n')

            elif account_act == '3':
                card_transfer_number = input('\nEnter card number: ')
                check = (card_transfer_number,)
                Simple_bank.cur.execute('SELECT * FROM card WHERE number=?', check)
                if card_transfer_number != card_number:
                    if self.luhn_check(card_transfer_number):
                        if len(Simple_bank.cur.fetchall()):
                            transfer = int(input('\nEnter how much money you want to transfer: '))
                            check = (card_number,)
                            Simple_bank.cur.execute('SELECT balance FROM card WHERE number=?', check)
                            # fetchall output is list and insides are tuples
                            if transfer <= Simple_bank.cur.fetchall()[0][0]:
                                change = (transfer, card_number)
                                Simple_bank.cur.execute('UPDATE card SET balance = balance - ? WHERE number = ?', change)
                                change = (transfer, card_transfer_number)
                                Simple_bank.cur.execute('UPDATE card SET balance = balance + ? WHERE number = ?', change)
                                Simple_bank.conn.commit()
                            else:
                                print('\nNot enough money!')
                        else:
                            print('\nSuch a card does not exist.')
                    else:
                        print('\nProbably you made mistake in the card number. Please try again!')
                else:
                    print("\nYou can't transfer money to the same account!")

            elif account_act == '4':
                change = (card_number, )
                Simple_bank.cur.execute('DELETE FROM card WHERE number=?', change)
                Simple_bank.conn.commit()
                print('\nThe account has been closed!')
                break

            elif account_act == '5':
                print('\nYou successfully logged out!\n')
                break

            elif account_act == '0':
                Simple_bank.account_exit = True
                break

            else:
                pass

    def action(self):
        while True:
            print('''1. Create an account
2. Log into account
0. Exit''')
            act = input()
            if act == '1':
                self.new_account()
            elif act == '2':
                self.login(input('Enter your card number: '), input('Enter your PIN: '))
                if Simple_bank.account_exit:
                    print('Bye!')
                    break
            elif act == '0':
                print('Bye!')
                break
            else:
                print('If you want to choose action, you should input numbers')


man = Simple_bank()