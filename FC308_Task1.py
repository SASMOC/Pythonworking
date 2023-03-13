import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    return random.choice(words)

def display_word(word, guessed_letters):
    output = ''
    for letter in word:
        if letter in guessed_letters:
            output += letter
        else:
            output += '-'
    return output

def play_game():
    word = choose_word()
    guessed_letters = set()
    max_incorrect_guesses = 6
    incorrect_guesses = 0
    
    while incorrect_guesses < max_incorrect_guesses:
        print('Secret word:', display_word(word, guessed_letters))
        print('Incorrect guesses left:', max_incorrect_guesses - incorrect_guesses)
        guess = input('Guess a letter: ').lower()
        if guess in guessed_letters:
            print('You already guessed that letter.')
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print('You won! The secret word was:', word)
                return
        else:
            incorrect_guesses += 1
            print('Incorrect guess.')
    
    print('You lost! The secret word was:', word)

while True:
    play_game()
    play_again = input('Do you want to play again? (y/n) ').lower()
    if play_again != 'y':
        break