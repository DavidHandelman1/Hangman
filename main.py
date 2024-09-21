from Hangman import Hangman
import random

def makeList():
    filePath = "words.txt"

    with open(filePath, 'r') as file:
        contents = file.read()

    contents = contents.split()
    
    return contents


def main():
    words = makeList()  # constructs list of words from txt file

    randIndex = random.randint(0, len(words) - 1)   # get random index for word
    
    game = Hangman(words[randIndex])    # instantiate game object with random word
    print("Missing more than 7 letters will lose the game.")

    while True:
        guessedLetter = game.getValidInput()    # get valid user input
        game.checkInput(guessedLetter)  # check input, update hidden letters if found
        
        if game.checkMisses():
            print("You missed too many letters, game over.")
            break   # game over lol
        game.display()  # show word with underscores and chosen letters
        
        if game.checkIfFull():  # check if there are no underscores left
            print("You won the game!")
            break   # game over lol


# Call the main function
if __name__ == '__main__':
    main()