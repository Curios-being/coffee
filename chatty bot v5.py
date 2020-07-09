def intro(bot_name, birth_year):
    print(f'''Hello! My name is {bot_name}.
I was created in {birth_year}.''')


def remind_me():
    print('Please, remind me your name.')
    print(f'What a great name you have, {input()}')


def guess_age():
    print('''Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

    # in curly braces is this formula: age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {(int(input()) * 70 + int(input()) * 21 + int(input()) * 15) % 105}; "
          "that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    # int(input()) - number that you want
    for i in range(0, int(input()) + 1):
        print(i, '!')


def test():
    print('''Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.''')
    while True:
        answer = int(input())
        if answer == 2:
            print('Completed, have a nice day!')
            break
        else:
            print('Please, try again.')


def end():
    print('Congratulations, have a nice day!')


intro('Yep', 2020)
remind_me()
guess_age()
count()
test()
end()
