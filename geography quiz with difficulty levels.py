# Questions organized by difficulty
quiz = {
    "easy": [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome", "Berlin"],
            "answer": "Paris"
        },
        {
            "question": "On which continent is Brazil located?",
            "options": ["Asia", "Europe", "South America", "Africa"],
            "answer": "South America"
        }
    ],
    "medium": [
        {
            "question": "Which country has the largest desert?",
            "options": ["Australia", "China", "Saudi Arabia", "Algeria"],
            "answer": "China"
        },
        {
            "question": "Which river flows through Baghdad?",
            "options": ["Nile", "Tigris", "Euphrates", "Amazon"],
            "answer": "Tigris"
        }
    ],
    "hard": [
        {
            "question": "What is the capital of Bhutan?",
            "options": ["Thimphu", "Kathmandu", "Dhaka", "Colombo"],
            "answer": "Thimphu"
        },
        {
            "question": "Which country has the most official languages?",
            "options": ["India", "South Africa", "Switzerland", "Belgium"],
            "answer": "South Africa"
        }
    ]
}

# Function to run the quiz
def start_quiz():
    level = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    if level not in quiz:
        print("Invalid difficulty level.")
        return

    score = 0
    questions = quiz[level]
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")
        choice = input("Enter the number of your answer: ")
        try:
            if q["options"][int(choice) - 1] == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("⚠️ Invalid answer.")
    print(f"\nYour final score: {score}/{len(questions)}")

# Start the quiz
start_quiz()
