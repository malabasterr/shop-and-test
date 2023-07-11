class IncorrectInput(Exception):
    pass

def is_isogram(given_word):

    lowercase = given_word.lower() # making sure all characters are in lowercase
    letters = [] # empty list to add characters to

    for letter in lowercase: 
        try:
            if letter.isalpha(): # checks that all characters are alphabetic letters
                if letter in letters: 
                    return False # if the letter is already in the list, it fails
                letters.append(letter) 
            return True # otherwise the letter is added to the list and it passes
        except ValueError:
            raise IncorrectInput
    
input_word = input("Let's test to see if your word is an isogram! What word would you like to try?")
is_isogram(input_word)