import random
import time

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

# Main function to run the quiz
def run_quiz():
    print("\nWelcome to the Mental Math Quiz!")
    difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
    
    score = 0
    total_questions = 5
    
    for i in range(total_questions):
        question, num1, num2, operator = generate_question(difficulty)
        start_time = time.time()
        
        answer, correct_answer = ask_question(question, num1, num2, operator)
        
        # Check if the answer is correct
        if abs(answer - correct_answer) < 0.01:  # Allow a small tolerance for floating-point division
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}")
        
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        print(f"Time taken: {time_taken} seconds\n")
    
    print(f"Quiz Finished! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    run_quiz()
