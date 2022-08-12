import json
import time

from logger import logger

ValidAnswers = ["A", "B", "C"]
ValidAnswerString = ""

for answer in ValidAnswers:  # Generate a string of valid answers to be printed if the user enters an invalid answer
    if ValidAnswers.index(answer) == len(ValidAnswers) - 1:
        ValidAnswerString += f"{answer}"
    else:
        ValidAnswerString += f"{answer}, "


def PrintQuestion(QuestionNumber, question, QuestionAnswerTable):
    print(f"Question {QuestionNumber}: {question}")
    print(f"A: {QuestionAnswerTable[question]['A']}")
    print(f"B: {QuestionAnswerTable[question]['B']}")
    # Only print C if there is an answer supplied for it
    if QuestionAnswerTable[question]['C'] != "":
        print(f"C: {QuestionAnswerTable[question]['C']}")


def QuizGame(username, log: logger):
    log.game = "Quiz"
    file = open("QuizQuestions.json", "r")
    # get the full QuestionAnswerTable from the JSON file
    QuestionAnswerTable = json.loads(file.read())
    file.close()  # close the JSON file, as it has been fully loaded into QuestionAnswerTable

    # Initialise variables
    QuestionNumber = 0
    CorrectAnswers = 0

    for question in QuestionAnswerTable:
        QuestionNumber += 1
        # Print the question
        try:
            PrintQuestion(QuestionNumber, question, QuestionAnswerTable)
        except Exception as e:  # If there is an error printing the json
            print("Error printing answers! Possible error in JSON formatting?")
            log.log(f"error: JSON formatting error, Error with field: {e}")
            return  # go back to the games menu
        while True:
            GuessedAnswer = input("Choose an answer: ")
            GuessedAnswer = GuessedAnswer.upper()
            if GuessedAnswer in ValidAnswers:  # If the guessed answer is valid
                break
            else:  # If the guessed answer is NOT valid (is invalid)
                log.log(
                    f"{GuessedAnswer} is not a valid answer, the valid answers are: {ValidAnswers}")
                print(
                    f"That's not a valid answer! Valid answers are: {ValidAnswerString}")

        if GuessedAnswer == QuestionAnswerTable[question]['Correct']:
            print()  # Print some blank lines to make the output easier to read
            print("Correct!")
            print()
            CorrectAnswers += 1
        else:
            print()
            print(
                f"Incorrect! The correct answer was {QuestionAnswerTable[question]['Correct']}")
            print()

    if CorrectAnswers == QuestionNumber:  # If the user got 100%
        print(
            f"Congratulations {username}! You got every single question right! That's {CorrectAnswers} questions in a row!")
    else:
        print(
            f"Congratulations {username}! You got {CorrectAnswers} out of {QuestionNumber} correct!")
    time.sleep(0.5)


# If the script is run directly, without the menu screen, use the username Developer
if __name__ == "__main__":
    QuizGame("Developer", logger())
