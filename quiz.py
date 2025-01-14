import random
import time
from colorama import Fore, Style
import os

# Function to generate a random question
def generate_question(difficulty):
    operators = ['+', '-', '*', '/']
    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 'medium':
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"

    return question, num1, num2, operator

# Function to ask the question and get the answer
def ask_question(question, num1, num2, operator):
    correct_answer = None
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 / num2

    answer = float(input(f"What is: {question} ? "))
    return answer, correct_answer

# Function to display a countdown timer
def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(Fore.YELLOW + f"Time left: {remaining} seconds" + Style.RESET_ALL, end="\r")
        time.sleep(1)
    print("\n")

# Function to read the high score from a file
def read_high_score():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

# Function to write the high score to a file
def write_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Main function to run the quiz
def run_quiz():
    from colorama import init
    init(autoreset=True)

    print(Fore.CYAN + "\nWelcome to the Mental Math Quiz!" + Style.RESET_ALL)
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()

    high_score = read_high_score()
    print(Fore.MAGENTA + f"Current High Score: {high_score}" + Style.RESET_ALL)

    score = 0
    total_questions = 5

    for i in range(total_questions):
        print(Fore.BLUE + f"\nQuestion {i + 1} of {total_questions}" + Style.RESET_ALL)
        question, num1, num2, operator = generate_question(difficulty)

        # Start a countdown timer
        timer_seconds = 10
        print(Fore.YELLOW + f"You have {timer_seconds} seconds to answer this question." + Style.RESET_ALL)
        countdown_timer(timer_seconds)

        start_time = time.time()
        try:
            answer, correct_answer = ask_question(question, num1, num2, operator)
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a number." + Style.RESET_ALL)
            continue

        # Check if the answer is correct
        if abs(answer - correct_answer) < 0.01:  # Allow a small tolerance for floating-point division
            print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + f"Wrong! The correct answer was {correct_answer}" + Style.RESET_ALL)

        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        print(Fore.MAGENTA + f"Time taken: {time_taken} seconds" + Style.RESET_ALL)

    print(Fore.CYAN + f"\nQuiz Finished! Your score: {score}/{total_questions}" + Style.RESET_ALL)

    if score > high_score:
        print(Fore.GREEN + "Congratulations! You beat the high score!" + Style.RESET_ALL)
        write_high_score(score)
    else:
        print(Fore.YELLOW + f"Try again to beat the high score of {high_score}!" + Style.RESET_ALL)

if __name__ == "__main__":
    run_quiz()