#Guess the Number Game by Nicole Alexander

#imports
import random

#variables
guesses = 10
number = random.randint(1, 100)
win = False

#conditional statements 
while guesses > 0:
    guess = int(input("Guess: "))

    guesses -= 1

    if guess > number:
        print("You guessed too high. You have " + str(guesses) + " remaining.")
    elif guess < number:
       print("You guessed too low. You have " + str(guesses) + " remaining.") 
    else:
        print("Congrats, you won! You guessed correctly!")
        print("Would you like to play again?")
        win = True

        while True:
            play_again = raw_input("yes or no: ")
            if play_again.lower() not in ('yes', 'no'):
                print("That's not 'yes' or 'no.'")
            else:
                break
 

if win == False:
    print("Sorry, you didn't guess the correct number. The correct number was" + ", " + str(number) + ".")
    print("Would you like to play again?")
while True:
    play_again = raw_input("yes or no: ")
    if play_again.lower() not in ('yes', 'no'):
        print("That's not 'yes' or 'no.'")
    else:
         break