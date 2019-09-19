import unittest


def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word: #loop through each char in secret_word
        if letter in letters_guessed: #each char in secret_word will be check if it is IN letters_guessed
            result += letter #if x from secret_word does exist in list of letters_guessed, then add it to our result
        else: #if x doesn't exist in our letters_guessed then append "_"
            result += "_"
    return result

def is_guess_in_word(guess, secret_word): #A function to check if the guessed letter is in the secret word
    return False if guess not in secret_word else True

def check_user_input(guessed_letter):
    if guessed_letter == "" or len(guessed_letter) > 1 or any(char.isdigit() or char.isspace() for char in guessed_letter): #while user doesn't enter anything OR user enter more than 1 character OR any character in user_input has digit or space, ask the user to change the input
        return "not accepted"
    return "accepted" #return the user input as a string

def play_again(user_input):
    if user_input != "y" and user_input != "Y" and user_input != "n" and user_input != "N":
        return "not y or n"
    return user_input

class GetSpacemanTests(unittest.TestCase):
    
    def test_get_guessed_word(self):
        self.assertEqual(get_guessed_word("word", "abczxy"), "____")
        self.assertEqual(get_guessed_word("secretword", "ghjjklword"), "___r__word") #should have 2 r's
        self.assertEqual(get_guessed_word("word", "word"), "word")
            
    def test_is_guess_in_word(self):
        self.assertEqual(is_guess_in_word("l", "secret_word"), False)
        self.assertEqual(is_guess_in_word("k", "Kobe"), False) #it should be false because k is small in Kobe
        self.assertEqual(is_guess_in_word("l", "love"), True)

    def test_check_user_input(self):
        self.assertEqual(check_user_input("h"), "accepted")
        self.assertEqual(check_user_input(""), "not accepted")
        self.assertEqual(check_user_input(" "), "not accepted")
        self.assertEqual(check_user_input("7"), "not accepted")
        self.assertEqual(check_user_input("y"), "accepted")
        self.assertEqual(check_user_input("n"), "accepted")

    def test_play_again(self):
        self.assertEqual(play_again("g"), "not y or n")
        self.assertEqual(play_again("f"), "not y or n")
        self.assertEqual(play_again("a"), "not y or n")
        self.assertEqual(play_again("5"), "not y or n")
        self.assertEqual(play_again("y"), "y")
        self.assertEqual(play_again("N"), "N")
        


if __name__ == "__main__":
    unittest.main()