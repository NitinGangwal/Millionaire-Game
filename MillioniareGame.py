
# Quiz Game in Python
# Questions, Options, aur Correct Answers list
# (Correct answer me 1, 2, 3, ya 4 ka use kiya hai)
questions = [
    {
        "question": "Who is Shah Rukh Khan?",
        "options": ["WWE Wrestler", "Plumber", "Actor", "Astronaut"],
        "answer": 3
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 2
    },
    {
        "question": "How many colors are there in a rainbow?",
        "options": ["5", "6", "7", "8"],
        "answer": 3
    },
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": 2
    },
    {
        "question": "Which animal is known as the 'Ship of the Desert'?",
        "options": ["Horse", "Camel", "Elephant", "Lion"],
        "answer": 2
    },
    {
        "question": "Which is the tallest animal on Earth?",
        "options": ["Giraffe", "Elephant", "Dinosaur", "Kangaroo"],
        "answer": 1
    },
    {
        "question": "What is the national fruit of India?",
        "options": ["Apple", "Banana", "Mango", "Grapes"],
        "answer": 3
    },
    {
        "question": "How many days are there in a normal year?",
        "options": ["360", "365", "366", "350"],
        "answer": 2
    },
    {
        "question": "Which is the smallest country in the world?",
        "options": ["India", "Vatican City", "Monaco", "Maldives"],
        "answer": 2
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Albert Einstein", "Thomas Edison", "Alexander Graham Bell", "Isaac Newton"],
        "answer": 3
    }
]

prizes = [100000, 5000, 2500, 1000, 30000, 10000, 12640, 24544, 41540, 3000]
score = 0

print("--- Welcome to the Quiz Game! ---")
print("Answer by entering 1, 2, 3, or 4.\n")

# Loop chala kar ek-ek karke questions poochna
i = 0
for i, q in enumerate(questions, 1):
    print(f"Question {i}: {q['question']}")
    print(f"1. {q['options'][0]}")
    print(f"2. {q['options'][1]}")
    print(f"3. {q['options'][2]}")
    print(f"4. {q['options'][3]}")
    
    # User se sahi input lena
    while True:
        try:
            user_answer = int(input("Enter your answer (1-4): "))
            if user_answer in [1, 2, 3, 4]: 
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, 3, or 4).")
            
    # Answer check karna
    if user_answer == q['answer']:
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was option {q['answer']}.\n")

# Final Results
print("--- Game Over ---")
print(f"Your final score is: {score}/{len(questions)}")

print("you won {prizes[i]}")
i+=1
