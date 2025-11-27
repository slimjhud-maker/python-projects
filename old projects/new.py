pupils = ["George", "Alex", "Joe", "Arthur"]

for i in pupils:
    print(i)

for i in range(len(pupils)):
    print(str(i + 1) + ": " + pupils[i])

pupils[2] = "Harry"

print(pupils)

pupils.remove("Arthur")

print(pupils)

pupils.append("Ron")

print(pupils)