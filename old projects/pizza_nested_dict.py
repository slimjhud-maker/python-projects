pizza = {"cheese" : {"small" : 5, "medium" : 7, "large" : 9},
        "margarita" : {"small" : 6, "medium" : 8, "large" : 10},
        "pepperoni" : {"small" : 11, "medium" : 13, "large" : 15},
        "chicken" : {"small" : 8, "medium" : 10, "large" : 12}}

stock = 100

print("Welcome to The Pizzeria \n")

for i,j in pizza.items():
    print("\n" + i)
    for m,n in j.items():
        print(m + ": " + str(n))


ptype = input("What pizza do you want? ").lower()
size = input("What size pizza do you want? ").lower()
if ptype in pizza:
    quant = int(input("How many pizzas do you want? "))
    if quant > stock:
        print("Not in stock")
    else:
        if size in ["small", "medium", "large"]:
            cost = quant * pizza[ptype][size]
            print("The cost is: " + str(cost))
        else:
            print("Size not found")
else:
    print("Pizza not found")
