count = 0
num_1 = int(input("Select a number to be the first number in your range: "))
num_2 = int(input("Select a number to be the last number in your range: "))
for i in range(num_1,num_2 + 1):
    if i % 2 == 0:
        count += 1
    else:
        count += 0
print("There are " + str(count) + " " + "even numbers in the range "  +  str(num_1) + " " + "to " + str(num_2))