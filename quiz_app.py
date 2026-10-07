from questions import questions

print("Welcome to the Current Affairs Quiz!")

score = 0

for number, question in enumerate(questions, 1):
    print(f"\nQuestion {number}: {question['question']}")

    for option, text in question["options"].items():
        print(f"{option}. {text}")

    answer = input("Choose your answer (A, B, C or D): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer:", question["answer"])

print("\nQuiz completed!")
print("Your score:", score, "out of", len(questions))
