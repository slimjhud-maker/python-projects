def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print("Assignment 1:", multiply_all(2, 3, 4))  