import sqlite3 as sql
import random

connection = sql.connect("quiz.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_scores(
        id INTEGER,
        name TEXT,
        score INTEGER
    )
""")
connection.commit()

python_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    },
    {
        "question": "What will print(len('Hello')) output?",
        "options": ["A. 4", "B. 5", "C. 6", "D. Error"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which function takes input from user?",
        "options": ["A. scan()", "B. read()", "C. input()", "D. get()"],
        "answer": "C"
    }
]

sql_questions = [
    {
        "question": "Which SQL command is used to retrieve data?",
        "options": ["A. INSERT", "B. UPDATE", "C. SELECT", "D. DELETE"],
        "answer": "C"
    },
    {
        "question": "Which command adds new data to a table?",
        "options": ["A. INSERT", "B. SELECT", "C. CREATE", "D. UPDATE"],
        "answer": "A"
    }
]

sorting_questions = [
    {
        "question": "Which algorithm repeatedly swaps adjacent elements?",
        "options": ["A. Bubble Sort", "B. Merge Sort", "C. Quick Sort", "D. Heap Sort"],
        "answer": "A"
    },
    {
        "question": "Which sorting algorithm uses divide and conquer?",
        "options": ["A. Bubble Sort", "B. Merge Sort", "C. Selection Sort", "D. Insertion Sort"],
        "answer": "B"
    }
]

all_questions = python_questions + sql_questions + sorting_questions


def take_quiz():
    name = input("Enter your name: ")
    quiz = random.sample(all_questions, 5)
    score = 0

    for q in quiz:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)

        ans = input("Your answer: ").upper()

        if ans == q["answer"]:
            score += 1

    print("\nYour score is:", score)

    cursor.execute("INSERT INTO quiz_scores(id, name, score) VALUES (?, ?, ?)",
                   (random.randint(1, 9999), name, score))
    connection.commit()
    print("Score saved!")


def display_scores():
    cursor.execute("SELECT * FROM quiz_scores")
    rows = cursor.fetchall()

    print("\n--- QUIZ SCORES ---")
    for x in rows:
        print(x)
    print("--------------------\n")


def delete_score():
    name = input("Enter name to delete score: ")
    cursor.execute("DELETE FROM quiz_scores WHERE name = ?", (name,))
    connection.commit()
    print("Score deleted!")


def modify_score():
    name = input("Enter name to update score: ")
    new_score = int(input("Enter new score: "))

    cursor.execute("UPDATE quiz_scores SET score = ? WHERE name = ?", (new_score, name))
    connection.commit()
    print("Score updated!")


while True:
    print("""
1. Take Quiz
2. Display Scores
3. Delete Score
4. Modify Score
5. Exit
""")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        take_quiz()
    elif choice == 2:
        display_scores()
    elif choice == 3:
        delete_score()
    elif choice == 4:
        modify_score()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")


cursor.close()
connection.close()