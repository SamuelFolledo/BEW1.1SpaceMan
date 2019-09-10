import random
from termcolor import colored #in order to user termcolor library

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    return False if guess not in secret_word else True
    # if guess not in secret_word:
    #     return False
    # else:
    #     return True




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    #TODO: show the player information about the game according to the project spec
    print("--------------------------------- Welcome to Space Man ---------------------------------")
    print(secret_word)
    number_of_chars = len(secret_word)
    i = 0
    global chances
    chances = number_of_chars

    # for x in secret_word:

    while i < number_of_chars:
        answer.append("_")
        i+=1
    for x in answer:
        print(x)
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letter = user_input("Guess the word: ")
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    if is_guess_in_word(letter, secret_word): #if guessed is in word...
        print("We have that letter")

    else: #if we dont have that letter
        print("WRONG!")
        chances -= 1
        print(chances)
        

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost
    while chances >= 0:
        letter = user_input("Guess the word: ")


def user_int_input(prompt): #for INT user input
    user_input = input((colored(prompt, "cyan"))) #grabs user input 
    while user_input == "" or len(user_input) > 1 or user_input.isdigit() == False: #ensures the input is an integer
        user_input = input(colored("Please enter a whole number only: ","red", attrs=['bold'])) #ask for user input again
    return int(user_input) #return the user_input as an integer

def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input((colored(prompt, "cyan"))) #user_input will equal to what the user inputted in a string format
    # while user_input == "" or user_input == " ": #ensures that the user does input a value and not just a blank or space
    while user_input == "" or len(user_input) > 1 or any(char.isdigit() or char.isspace() for char in user_input): #while user doesn't enter anything OR user enter more than 1 character OR any character in user_input has digit or space, ask the user to change the input
        user_input = input(colored("Please input 1 letter only: ", "red", attrs=['bold'])) #ask for the input again
    return user_input #return the user input as a string




#These function calls that will start the game
secret_word = load_word()
answer = []
life = 7
spaceman(secret_word)
