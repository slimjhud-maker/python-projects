nums = [10, 15, 30, 42, 55, 60, 75]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))

print("Assignment 4:", divisible)   