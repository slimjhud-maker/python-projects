larger = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Larger number is:", larger(num1, num2))