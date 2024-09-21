class Hangman:

    word = ""   # word used as key
    userDisplay = []    # will initially show underscores
    guessedLetters = set()  # unordered set
    missed = 0

    def __init__(self, word):
        self.word = word
        for i in range(len(word)):  # initialize with underscores
            self.userDisplay.append('_')

    def display(self):
        print(f"You have { 8 - self.missed } misses left.")
        for c in self.userDisplay:
            print(c,  end=' ')
        print("\n")

    def getValidInput(self):
        while True:
            guessed = input("Guess a lowercase letter: ")
            
            if len(guessed) == 1: # only want one letter

                if guessed.islower(): # a - z range on ascii table
                    if guessed in self.guessedLetters:  # letter already guessed
                        print("Already guessed letter " + guessed + "!")
                        continue
                    else:
                        self.guessedLetters.add(guessed)    # add to set
                        return guessed  # valid input a - z, lowercase char
                    
                else:   # not lowercase letter
                    print("Must guess a lowercase letter!")
                    continue   
                     
            else:   # length of input != 1
                print("Guess ONE letter!")
                continue

    def checkInput(self, guess):
        found = False

        for i in range(0, len(self.word)):
            if self.word[i] == guess:
                self.userDisplay[i] = guess     # make letter visible
                found = True    # letter was found

        if found:
            print("Letter " + guess + " was in word.")
        else:
            print("Letter " + guess + " was not in word.")
            self.missed += 1     # letter not found, so increment missed

    def checkMisses(self):
        if self.missed > 7:
            return True     # too many misses, game over
        else:
            return False    # user can still miss letter(s), continue game

    def checkIfFull(self):
        for c in self.userDisplay:
            if c == '_':
                return False    # still at least one underscore
        
        return True     # no underscores left