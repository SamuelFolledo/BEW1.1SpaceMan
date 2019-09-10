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
    result = ""
    # if letters_guessed not in secret_word: #if each characters in letters_guessed is not in secret_word, then user got a wrong letter
    
    for x in secret_word: #loop through each char in secret_word
        if x in letters_guessed: #each char in secret_word will be check if it is IN letters_guessed
            result += x #if x from secret_word does exist in list of letters_guessed, then add it to our result
        else: #if x doesn't exist in our letters_guessed then append "_"
            result += "_"
    return result



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




def spaceman(secret_word): # A function that controls the game of spaceman. Will start spaceman in the command line.

#TODO: show the player information about the game according to the project spec
    print("--------------------------------- Welcome to Space Man ---------------------------------")
    secret_word = secret_word.upper() #capitalize all the letters or secret word
    print(secret_word)
    
    secret_array = [] #will contain our player's progress
    letters_guessed = ""

    for _ in secret_word: #fill our array with "_"
        secret_array.append("_")
    

    # i = 0
    number_of_chars = len(secret_word)
    global chances
    chances = number_of_chars
    won = False
    # print("\n")


    while chances > 0 and won == False: #while we still have life and won is false... keep playing the game
#TODO: Ask the player to guess one letter per round and check that it is only one letter
        guess = user_input("Guess the word: ").upper() #Grabs user input and capitalize it
        while letters_guessed.find(guess) != -1: #if our user use a letter they have used before, then ask the user to try another letter
            guess = user_input(colored("Letter ", "red") +guess+ colored(" has been used before. Please try another letter: ","red")).upper() #Gives a red warning sign, and capitalize the accepted guess
        letters_guessed += guess #append/add our guess to letters_guessed

#TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word) == False: #if guess does not exist in secret_word, then subtract HP
            print("WRONG!")
            chances -= 1

        print("You have "+str(chances)+" chances left") #print lives left
        for letter in letters_guessed: #print letters guessed
            print(letter, end=", ")
        print("\n")

#TODO: show the guessed word so far
        guessed_word = get_guessed_word(secret_word, letters_guessed) #get our current round's guessed_word
        # print("Guessed word is "+guessed_word+ " Secret word is "+secret_word)
        for letter in guessed_word:
            print(letter, end=" ") #prints guessed_word
        print("\n")

        if guessed_word == secret_word: #if our returned guessed_word is the same as our secret_word, then user won!
            won = True

#TODO: check if the game has been won or lost
    if won == True:
        print("Congrats! You won!")
    else:
        print("Sorry you lost, the secret word was "+secret_word)

    rematch = user_input("Would you like to play again? Select (y/n): ")
    while(rematch != "y" or rematch != "Y" or rematch >= "n" or rematch != "N"):
        rematch = ("Please enter Y for yes to play again, or N if not")

    if rematch == "Y" or user_input == "y":
        play_again()

def play_again():
    spaceman(load_word)


def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input((colored(prompt, "cyan"))) #user_input will equal to what the user inputted in a string format
    # while user_input == "" or user_input == " ": #ensures that the user does input a value and not just a blank or space
    while user_input == "" or len(user_input) > 1 or any(char.isdigit() or char.isspace() for char in user_input): #while user doesn't enter anything OR user enter more than 1 character OR any character in user_input has digit or space, ask the user to change the input
        user_input = input(colored("Please input 1 letter only: ", "red", attrs=['bold'])) #ask for the input again
    return user_input #return the user input as a string




#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
