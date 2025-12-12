import random 
num = random.randint(1,100) # creates range of 1 to 100
while True:
    user_num = int(input("Pick a number from 1 to 100: ")) # asking user to pick a number
    if user_num == num: # checking if the user's number is the same as the random number
        print("Correct! Well Done") 
        break
    elif user_num > num: # checking if the user's number is the larger than the random number 
        print("\nToo high. Guess lower next time\n")
    elif user_num < num: # checking if the user's number is the smaller than the random number
        print("\nToo low. Guess higher next time\n")
    else:
        print("\nPlease input a number\n")