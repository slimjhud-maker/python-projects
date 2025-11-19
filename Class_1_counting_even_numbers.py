count = 0 # setting the amount of even numbers to 0
num_1 = int(input("Select a number to be the first number in your range: ")) # user will input the first number of the range
num_2 = int(input("Select a number to be the last number in your range: "))  # user will input the last number of the range
for i in range(num_1 + 1,num_2): # creating the range with range function. Add 1 to num_2 
    if i % 2 == 0:
        count += 1
    else:
        count += 0
print("There are " + str(count) + " " + "even numbers in the range "  +  str(num_1) + " " + "to " + str(num_2))