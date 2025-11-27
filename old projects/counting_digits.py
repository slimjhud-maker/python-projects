num = int (input("Enter a number: "))
ognum = num
count = 0
while num > 0:
    count += 1
    num //= 10

print("The number " + str(ognum) + " " + "has " + str(count) + " " + "digits in it" )