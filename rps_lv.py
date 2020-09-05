import random


def update_rating(name):
    data = retrieve_the_data()
    if name in data:
        data[name] = str(user_rating)
    else:
        data.update({name: str(user_rating)})
    insert_the_data(data)


def retrieve_the_data():
    rating = open('rating.txt', 'r')
    data = {}
    for i in rating.readlines():
        # it makes list with such construction [name, result]
        line = i.rstrip('\n').split()
        # it makes dict with such construction {name: result, name: result} used dict comprehension
        data.update({line[0]: line[1]})
    rating.close()
    return data


def insert_the_data(data):
    rating = open('rating.txt', 'w')
    for user in data:
        print(user + ' ' + data[user], file=rating, end='\n')
    rating.close()


def check_rating(user):
    for line in rating:
        if line[:len(user)].lower() == user:
            return int(line[len(user) + 1:])
    return 0


def game(move):

    choice = random.choice(options)
    # basically, just index of element
    counter = -1
    for i in options:
        counter += 1
        if move == i:
            break
    # welp, slicing from the end to the beginning seems to be impossible, so that's it (
    other_elements = options[(counter - len(options) + 1):] + options[:counter]
    # tried to make for even number also, came up that there're should be 2 draws, otherwise no balance
    # at least i see so
    if move == choice:
        print(f'There is a draw({choice})')
        return 50
    elif len(options) % 2 == 0 and choice == other_elements[len(other_elements) // 2]:
        print(f'There is a draw({choice})')
        return 50
    elif choice in other_elements[:len(other_elements) // 2]:
        print(f'Sorry, but the computer chose {choice}')
        return 0
    else:
        print(f'Well done. The computer chose {choice} and failed')
        return 100


name = input('Enter your name: ')
print(f'Hello, {name}!')
choice = input().split(',')
if len(choice) < 3:
    options = ['scissors', 'rock', 'paper']
else:
    options = choice
print("Okay, let's start")
rating = open('rating.txt', 'r')
user_rating = check_rating(name.lower())
rating.close()

while True:

    act = input()

    if act == '!rating':
        print(f'Your rating: {user_rating}')
    elif act == '!exit':
        print('Bye!')
        break
    elif act not in options:
        print('Invalid input')
    else:
        user_rating += game(act, )

update_rating(name)