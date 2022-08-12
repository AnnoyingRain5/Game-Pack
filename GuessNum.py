import random
import time

from logger import logger


def GuessingGame(username, log: logger):
    log.game = "Guessing Game"
    # Initialization
    guess = None
    guessAmount = 0
    print("What numbers would you like to guess between?")
    # input validation
    while True:
        MaxNum = input("I would like to guess between 1 and ")
        if MaxNum.isdigit():
            MaxNum = int(MaxNum)
            break
        else:
            print("Please enter a valid number")
            log.log(f"{MaxNum} is not a digit")
    TargetNumber = random.randint(1, MaxNum)
    # Main game loop
    while guess != TargetNumber:
        # Get input and do input validation
        guess = input(f"Guess a number between 1 and {MaxNum}: ")
        if guess.isdigit():  # If the guess is a number
            guess = int(guess)
            if guess > MaxNum:  # if the number is in the acceptable range
                print(f"Your guess needs to be between 1 and {MaxNum}")
                log.log(f"{guess} is not between 1 and {MaxNum}")
                continue  # Start the loop from the beginning again without running any of the below code'
        else:
            print("Your guess must be a number")
            log.log(f"{guess} is not a digit")
            continue  # Start the loop from the beginning again without running any of the below code

        # Check guess against TargetNumber and provide feedback
        guessAmount += 1
        if guess == TargetNumber:
            if guessAmount == 1:  # If the user got it on the first try
                print("Amazing! You got it on the first try!")
            print(
                f"Congratulations {username}! You took {guessAmount} guesses!")
            time.sleep(0.5)  # give the user time to read the message
            break  # go back to the menu
        # give the user feedback
        elif guess > TargetNumber:
            print("Lower!")
        elif guess < TargetNumber:
            print("Higher!")


# If the script is run directly, without the menu screen, use the name Developer
if __name__ == "__main__":
    GuessingGame("Developer", logger())
