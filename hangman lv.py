import random

print("H A N G M A N")
word_list = ['python', 'java', 'kotlin', 'javascript']

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        word = random.choice(word_list)
        guess = '-' * len(word)
        letters = set(word)
        used_letters = set()
        attempts = 0
        while True:
            print(f'\n{guess}')
            if guess.count('-') == 0:
                print('''You guessed the word!
You survived!\n''')
                break

            letter = input('Input a letter: ')

            if len(letter) > 1:
                print('You should input a single letter')
            elif not letter.islower():
                print('It is not an ASCII lowercase letter')
            elif letter in letters:
                guess = ''.join([letter if word[i] == letter else guess[i] for i in range(len(guess))])
                letters.discard(letter)
                used_letters.update(letter)
            elif letter in used_letters:
                print('You already typed this letter')
            else:
                print('No such letter in the word')
                attempts += 1
                used_letters.update(letter)
            if attempts == 8:
                print('You are hanged!\n')
                break
    elif choice.lower() == 'exit':
        break
