# Import modules
import time
import random
import string
#import github.com/lyndonwatkins

# Initialise variables
wordlist = ["adduct","adjust","absurd","acquit","badger","bicker","bought","branch","earwig",
    "dollar","bounce","fabric","harmed","eating","lizard",]
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Clear the screen and intro...
print ("\n" * 100)
play=input("Would you like to play a game? (Yes/No) ")

# Process input (lowercase) yes or y will suffice
if str.lower(play)=="yes" or str.lower(play)=="y":
    play=True
else:
    play=False

# Play the game
while play==True:
    time.sleep

    # Initialise game specific variables
    guessed = ""
    randomWord = random.choice(wordlist)
    blanks = "_ " * len(randomWord)
    newBlanks = ""


    print ("\nWord: ",blanks)
    lives = 6
    while lives > 0:

        # Iterate while there are still lives left...
        guess = input ("\nPlease make a guess: ")
        guessed += guess

        # Check if the letter has already been guessed.
        if guess in newBlanks:
            print("You've already guessed that one!")
            newBlanks = " ".join(i if i in guessed else "_" for i in randomWord)
            if guess==randomWord:
                print("Correct")
                play=True
                lives=0
                break
        # This code has been copied from github.com/lyndonwatkins
        # and is not a student product!
        while guess not in alphabet:
           print ("Please only enter letters")
           guess = input ("Please make a guess: ")
        while len(guess)>1:
            print("Only one letter at a time")
            guess = input ("Please make a guess: ")
        for letters in guess:
            newBlanks = " ".join(i if i in guessed else "_" for i in randomWord)

            if guess in randomWord:
                newBlanks = " ".join(i if i in guessed else "_" for i in randomWord)
                print("Word: ",newBlanks)
                print ("Guess is correct!")
            else:
                lives-=1
                print ("Oops, got one wrong!  You have ", lives, " lives left!")
                newBlanks = " ".join(i if i in guessed else "_" for i in randomWord)
                print("Word: ",newBlanks)
            if ("_") not in newBlanks:
                print("You have won!")
                play=True
                lives=0
                break

    while lives==0:
        print()
        import time
        time.sleep(1)
        print("The word was: ",randomWord)
        print()
        import time
        time.sleep(1)
        again=input("Would you like to play again? Yes/No: ")
        if str.lower(again)=="no":
            play=False
            lives=0
            break
        else:
            lives=1
            play=True
