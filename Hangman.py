import random

def main():

    word = "ido is"

    guesses = []
    num_of_gusses = guesses.count

    puzzleWord = makeWordAPuzzle(word)

    CurrentGuess = chr(input("Enter a word: "))

    #if(guesses.find(CurrentGuess) is True):
        #CurrentGuess = chr(input("Already chose this letter"))



    print(guesses)





def makeWordAPuzzle(word):
    newsequence = wo

    for x in word:
        if x is " ":
            newsequence.__add__(" ")
        else:
            newsequence.__add__("_")
    return newsequence









if __name__ == '__main__':
    main()
