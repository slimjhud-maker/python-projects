questions = {"What is 1+1?": "2", "What is the capital of Germany?": "Berlin", "What is 2+2?": "4", "What is the capital of the UK?": "London"}

score = 0

for i, j in questions.items():
    ans = input(i + ": ")
    if ans.lower() == j.lower():
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("Your score is:" + str(score))