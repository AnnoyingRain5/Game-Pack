import random
import time

from logger import logger

# A list of all the standard possibilities in the maze
MazePossibilities = [
    "The road splits off into many directions ahead, which way to go?",
    "What a large opening! There appears to be something glimmering ahead in the distance, but that might just be your imagination....",
    "The walls appear to be closing in as we move ahead, is this still the right path?",
    "Everything seemed to go dark for a moment, but its fine now, is going ahead still a great idea?",
    "You hit your head as you were making your way through a narrow corridor",
    "You somehow stubbed your toe when making your way down a steep set of stairs, but you made it to the bottom without too much more trouble",
    "Ahead there are four choices, two staircases going down, one going up, or you could turn back, which way do you go?",
    "The ground seems to be painted strangely ahead, is it safe to continue down this path?",
    "The path appears to be clear ahead",
    "This part of the maze appears to have a clear view of the sky... strange..."
]
Controls = "Controls: Forward, Backward, Left, Right and Exit"
prompt = "Which way to go now? "

InvalidInput = False
# A class that controls most of the user input for the game


class Direction:
    # create empty classes, as the classes dont need functionality, just to be compared to each other
    # for example, direction1 = Direction.Left, Direction2 = Direction.Right, direction1 != direction2
    class Forward:
        pass

    class Backward:
        pass

    class Left:
        pass

    class Right:
        pass

    def FromString(dir):
        dir = dir.capitalize()
        match dir:
            case "Forward":
                return Direction.Forward
            case "Backward":
                return Direction.Backward
            case "Left":
                return Direction.Left
            case "Right":
                return Direction.Right
            case "Exit":
                return "ExitGame"
            case _:  # Underscore in a match statement is a catchall, will essentially work as a catch for invalid input
                global InvalidInput
                InvalidInput = True
                # Pick and return a random direction
                match random.randint(0, 3):
                    case 0:
                        return Direction.Forward
                    case 1:
                        return Direction.Backward
                    case 2:
                        return Direction.Left
                    case 3:
                        return Direction.Right

    def IsOpposite(Dir1, Dir2):  # check if one direction is the opposite of another
        if Dir1 == Direction.Forward and Dir2 == Direction.Backward:
            return True
        elif Dir1 == Direction.Left and Dir2 == Direction.Right:
            return True
        elif Dir1 == Direction.Backward and Dir2 == Direction.Forward:
            return True
        elif Dir1 == Direction.Right and Dir2 == Direction.Left:
            return True
        else:
            return False  # If it is not the opposite, return false


def clear():
    for i in range(10):
        print()
    global InvalidInput
    if InvalidInput == True:
        print("Invalid input, picking a direction at random...")
        print()
        InvalidInput = False


def MazeGame(username, log: logger):
    log.game = "Maze Game"

    # Introduction to game
    clear()
    print("You enter the maze at a fork in the road, you are told there is something on the other side, but you have no idea what.")
    print()
    print("This is a constantly shifting maze, even retracing your footsteps won't help you here...")
    DeadEnd = False
    ExitAhead = False
    while True:
        print()
        print(Controls)
        print()
        UserInput = Direction.FromString(input(prompt))
        clear()
        if UserInput == "ExitGame":  # If the user requested to exit the game
            print(
                'The floor collapsed under you after you said the sacred words, “Exit Game." Game over!')
            break
        RandomNumber = random.randint(0, len(MazePossibilities)-1)
        # Get a 1 in len(MazePossibilities) chance of entering getting a special flag added to your session
        if RandomNumber == 0:
            ExitRandomNumber = random.randint(0, 2)
            match ExitRandomNumber:
                case 0:
                    if DeadEnd == False:
                        print("You have hit a dead end")
                        DeadEnd = True
                    else:
                        print(
                            "The exit appears to be ahead, but something appears to be blocking the path")
                        print(
                            "you can attempt to push forward but it may not be the best idea...")
                        ExitAhead = True
                case 1:
                    if ExitAhead == False:
                        print(
                            "The exit appears to be ahead, but something appears to be blocking the path")
                        print(
                            "you can attempt to push forward but it may not be the best idea...")
                        ExitAhead = True
                    else:
                        print(MazePossibilities[RandomNumber])
                case 2:
                    print(
                        f"Congratulations {username}! You have found the exit!")
                    break  # The user has won, go back to the menu
        else:
            Event = MazePossibilities[RandomNumber]
            print(Event)
            if ExitAhead == True:
                print(Controls)
                UserInput = Direction.FromString(input(prompt))
                if UserInput == Direction.Forward:
                    print(
                        "The floor caved in under you, it was never designed to hold this much weight, it must have been a trap!")
                    print("You fell through the floor and died!")
                    break  # The user has died, go back to the menu
                else:
                    if UserInput == Direction.Left or UserInput == Direction.Right:
                        print(Controls)
                        NewUserInput = Direction.FromString(input(prompt))
                        if Direction.IsOpposite(UserInput, NewUserInput):
                            print(
                                f"Congratulations {username}! You have found the exit!")
                            break  # The user has won, go back to the menu
                        else:
                            print(
                                "The floor caved in under you, it was never designed to hold this much weight, it must have been a trap!")
                            print("You fell through the floor and died!")
                            break  # The user has died, go back to the menu
                    else:
                        print(MazePossibilities[RandomNumber])
                print(Controls)
    time.sleep(0.5)


# If the script is run directly, without the menu screen, use the name Developer
if __name__ == "__main__":
    MazeGame("Developer", logger())
