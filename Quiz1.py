quesans = ["What is 1+1?", "2", "What is the capital of Germany?", "Berlin", "What is 2+2?", "4", "What is the capital of the UK?", "London"]
score = 0
x = 0

while(x < len(quesans)):
    ans = input(quesans[x] + ": ")
    if ans.lower() == quesans[x+1].lower():
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
    x += 2

print("Your score is: " + str(score))

