print("Hello Welcome To The Quiz")

score = 0
questions = ["What is the capital of the UK?", "What is the capital of the USA?", "What is 1+1?", "What is 2+2?"]

answers = ["London", "Washington D.C", "2", "4"]

"""
ans = input("What is the capital of the UK?")
if ans == "London":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

ans = input("What is the capital of the USA?")
if ans == "Washington D.C":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
"""

x = len(questions)

for i in range(x):
    ans = input(questions[i] + ": ")
    if ans == answers[i]:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")


print("Your score is: " + str(score))