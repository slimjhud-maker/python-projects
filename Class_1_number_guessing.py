import random
num = random.randint(1,100)
while True:
    user_num = int(input("Pick a number from 1 to 100: "))
    if user_num == num:
        print("Correct! Well Done")
        break
    elif user_num > num:
        print("\nToo high. Guess lower next time\n")
    elif user_num < num:
        print("\nToo low. Guess higher next time\n")
    else:
        print("\nPlease input a number\n")