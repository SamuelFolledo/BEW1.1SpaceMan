import random
from termcolor import colored #in order to user termcolor library

def load_word(): #loads a random secret_word from words.txt
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word: #loop through each char in secret_word
        if letter in letters_guessed: #each char in secret_word will be check if it is IN letters_guessed
            result += letter #if x from secret_word does exist in list of letters_guessed, then add it to our result
        else: #if x doesn't exist in our letters_guessed then append "_"
            result += "_"
    for letter in letters_guessed: #print letters guessed
        print(letter, end=", ")
    print("\n")
    for character in result:
        print(character, end=" ") #prints guessed_word with spaces in between each character
    return result

def is_guess_in_word(guess, secret_word): #A function to check if the guessed letter is in the secret word
    return False if guess not in secret_word else True
    
def spaceman(secret_word): # A function that controls the game of spaceman. Will start spaceman in the command line.
    play = True
    word = secret_word.upper() #capitalize all the letters or secret word
#TODO: show the player information about the game according to the project spec
    while play:
        print("--------------------------------- Welcome to Space Man ---------------------------------")
        letters_guessed = ""
        chances = len(word)
        won = False
        get_guessed_word(word, letters_guessed) #get guessed word and print our "_" and chances left
        print(word)
        while chances > 0 and won == False: #while we still have life and won is false... keep playing the game
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
            guess = user_input("\nGuess the word: ").upper() #Grabs user input and capitalize it
            while letters_guessed.find(guess) != -1: #if our user use a letter they have used before, then ask the user to try another letter
                guess = user_input(colored("Letter ", "red") +guess+ colored(" has been used before. Please try another letter: ","red")).upper() #Gives a red warning sign, and capitalize the accepted guess
            letters_guessed += guess #append/add our guess to letters_guessed
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
            if is_guess_in_word(guess, word) == False: #if guess does not exist in secret_word, then subtract HP
                print(colored("WRONG!",attrs=['bold'])) #print wrong in bold
                chances -= 1 #decrement chances
            print("You have "+str(chances)+" chances left") #print lives left
            

    #TODO: show the guessed word so far
            guessed_word = get_guessed_word(word, letters_guessed) #get our current round's guessed_word
            if guessed_word == word: #if our returned guessed_word is the same as our secret_word, then user won!
                won = True

    #TODO: check if the game has been won or lost
        if won == True:
            print("\nCongrats! You won with "+str(chances)+" chances left!")
        else:
            print("Sorry you lost, the secret word was "+word)

    #STRETCH: Rematch
        rematch = play_again()
        if rematch == "n" or rematch == "N":
            play = False
        else:
            word = load_word().upper()

def user_input(prompt): #this method will display a message in the terminal and wait for user input
    user_input = input((colored(prompt, "cyan"))) #user_input will equal to what the user inputted in a string format
    # while user_input == "" or user_input == " ": #ensures that the user does input a value and not just a blank or space
    while user_input == "" or len(user_input) > 1 or any(char.isdigit() or char.isspace() for char in user_input): #while user doesn't enter anything OR user enter more than 1 character OR any character in user_input has digit or space, ask the user to change the input
        user_input = input(colored("Please input 1 letter only: ", "red", attrs=['bold'])) #ask for the input again
    return user_input #return the user input as a string

def play_again():
    rematch = user_input("Would you like to play again? Select (y/n): ")
    while rematch != "y" and rematch != "Y" and rematch != "n" and rematch != "N":
        rematch = user_input(colored("Please enter Y for yes to play again, or N if not ", "red"))
    return rematch
    

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
