class IncorrectInput(Exception):
    pass

def is_isogram(given_word):
    lowercase = given_word.lower() # making sure all characters are in lowercase
    letters = [] # empty list to add characters to

    for letter in lowercase: 
        if not letter.isalpha(): # checks that all characters are alphabetic letters
            raise IncorrectInput("Invalid input: Non-alphabetic characters detected.")
        if letter in letters: 
            return False # if the letter is already in the list, it fails
        letters.append(letter) 

    return True # if the loop completes without returning False, it is an isogram

input_word = input("Let's test to see if your word is an isogram! What word would you like to try?")
print(is_isogram(input_word))