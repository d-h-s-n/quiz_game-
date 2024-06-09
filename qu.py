def ask_question(question, options, correct_answer):
    print("\n" + question)
    for option in options:
        print(f"- {option}")
    
    while True:
        answer = input("Type your answer: ").strip().lower()
        if answer in [option.lower() for option in options]:
            break
        else:
            print(f"Invalid choice. Please type one of the following options: {', '.join(options)}.")

    if answer == correct_answer.lower():
        print("Correct!")
        return 3
    else:
        print(f"{answer} is Incorrect. The correct answer is {correct_answer}.")
        return -1

def run_quiz(questions):
    score = 0
    for question, data in questions.items():
        score += ask_question(question, data['options'], data['answer'])
        print(f"Your current score is: {score}")
    return score

def main():   
    # Define the quiz questions, options, and correct answers
    questions = {
        "What is the capital of France?": {
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "answer": "Mars"
        },
        "When was Indian national Anthem first sung?": {
            "options": ["Aug15th 1947", "Jan26th 1950", "Dec27th 1911", "None of the above"],
            "answer": "Dec27th 1911"
        },
        "In which country is the Chernobyl nuclear plant located?": {
            "options": ["Russia", "Ukraine", "India", "Nepal"],
            "answer": "Ukraine"
        }
    }

    print(  " \nHello There, Welcome to the Quiz Game !!\n") 
    play_game = input("Do you want to play the quiz game? (y/n): ").strip().lower()

    if play_game in ('yes', 'y'):
        score = run_quiz(questions)
        print(f"\nYour final score is: {score} out of {3 * len(questions)}.")
        print( "\nThank you for your Time ... \n")
    else:
        print("Thank you! You can quit the game.")

if __name__ == "__main__":
    main()
