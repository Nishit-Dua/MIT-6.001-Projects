# Problem Set 2, hangman.py
# Name: Nishit
# Collaborators: None
# Time spent: Way more that i needed to lmao

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
letters_guessed = []


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in
    letters_guessed; False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    '''
    message = ''
    for c in secret_word:
        if c not in letters_guessed:
            message += '_'
        else:
            message += c
    return message


def feedback(my_word, guess):
    if guess not in secret_word+'*':
        print(f'Sorry {guess} is not in Secret Word')
    else:
        print(f'YAY! {guess} is in Secret Word')
    print(my_word)


def guesser(letters_guessed):
    guess = input('Make a Guess: ')
    guess = guess.lower()
    while guess not in string.ascii_lowercase:
        guess = input('Enter a Valid letter: ')
    while guess in letters_guessed:
        guess = input('Already Guessed choose something else : ')
    return guess


def guesserWithHints(letters_guessed, my_word):
    guess = input('Make a Guess: ')
    if guess == '*':
        print('\nMatching Words in Word List:\n')
        show_possible_matches(my_word)
        print('\n')
        return guess
    else:
        guess = guess.lower()
        while guess not in string.ascii_lowercase:
            guess = input('Enter a Valid letter: ')
        while guess in letters_guessed:
            guess = input('Already Guessed choose something else : ')
        return guess


def WinLose(NUM_GUESSES, secret_word, my_word):
    if NUM_GUESSES == 0:
        print('\nYou Lost :(\n')

    if secret_word == my_word:
        print(f'\nYou Won my friend with {NUM_GUESSES} guesses remaining\n')


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    NUM_GUESSES = 6
    print(f'\nYour word has {len(secret_word)} letters and you\
 have {NUM_GUESSES} guesses to guess the word')

    while (not is_word_guessed(secret_word, letters_guessed))\
            and NUM_GUESSES != 0:
        print(f'\nyou have {NUM_GUESSES} guesses left')

        guess = guesser(letters_guessed)
        letters_guessed.append(guess)

        if guess not in secret_word:
            NUM_GUESSES -= 1

        my_word = get_guessed_word(secret_word, letters_guessed)
        feedback(my_word, guess)

    WinLose(NUM_GUESSES, secret_word, my_word)

    # When you've completed your hangman function, scroll down to the bottom
    # of the file and uncomment the first two lines to test
    # (hint: you might want to pick your own
    # secret_word while you're doing your own testing)

    # -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
    corresponding letters of other_word, or the letter is the special symbol
    _ , and my_word and other_word are of the same length; False otherwise
    '''
    if len(other_word) == len(my_word):
        L = [c for c in other_word]
        for c in my_word:
            if (c != '_') and c != L[my_word.index(c)]:
                return False
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches
    my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    '''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check
      that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    NUM_GUESSES = 6
    print(f'\nYour word has {len(secret_word)} letters and you\
 have {NUM_GUESSES} guesses to guess the word')
    my_word = get_guessed_word(secret_word, letters_guessed)
    while (not is_word_guessed(secret_word, letters_guessed))\
            and NUM_GUESSES != 0:
        print(f'\nyou have {NUM_GUESSES} guesses left')

        guess = guesserWithHints(letters_guessed, my_word)
        letters_guessed.append(guess)

        if guess not in secret_word:
            NUM_GUESSES -= 1

        my_word = get_guessed_word(secret_word, letters_guessed)
        feedback(my_word, guess)

    WinLose(NUM_GUESSES, secret_word, my_word)


# When you've completed your hangman_with_hint function, comment the two simila
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
