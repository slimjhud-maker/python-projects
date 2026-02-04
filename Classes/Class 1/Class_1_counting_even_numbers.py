count = 0 # setting the amount of even numbers to 0
num_1 = int(input("Select a number to be the first number in your range: ")) # user will input the first number of the range
num_2 = int(input("Select a number to be the last number in your range: "))  # user will input the last number of the range
for i in range(num_1,num_2 + 1): # creating the range with range function. Add 1 to num_2 or because computers count from 0
    if i % 2 == 0: # using the modulus function to find out if the remainder is 0
        count += 1 # adding 1 to the count of even numbers
    else:
        count += 0 # a remainder of 1 so add nothing to the count of even numbers
print("There are " + str(count) + " " + "even numbers in the range "  +  str(num_1) + " " + "to " + str(num_2)) # using the print function to print out the count of even numbers