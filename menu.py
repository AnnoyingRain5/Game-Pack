# menu program
import time

import GuessNum
import Maze
import Quiz
from logger import logger

log = logger()


def login():
    global username
    username = input(
        "Please enter a username, this username will be used throughout the games in the pack: ")
    print(f"Welcome {username}!")
    time.sleep(0.5)


def mainmenu():
    choice = 0
    while choice != "4":
        log.game = "Menu"

        # Print menu screen
        print("*****************************************")
        print()
        print("Choose an option from the following menu: ")
        print()
        print("1 - Text-based Maze Game")
        print("2 - Guessing Game")
        print("3 - Quiz")
        print("4 - Exit")
        print()
        print("******************************************")
        print()
        choice = input("Enter 1, 2, 3 or 4: ")

        match choice:
            case "1":
                print()
                print("Now running Maze game...")
                Maze.MazeGame(username, log)
            case "2":
                print()
                print("Now running Guessing game...")
                GuessNum.GuessingGame(username, log)
            case "3":
                print()
                print("Now running Quiz...")
                Quiz.QuizGame(username, log)
            case "4":
                print("Thanks for using the program.")
                log.exit()
            case _:
                print("Please enter 1,2,3 or 4")
                log.log(f"error: {choice} is not a valid menu option")


login()
mainmenu()
