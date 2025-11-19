pizzas = {"margarita" : 10, "cheese" : 9, "pepperoni" : 15, "chicken" : 12}
stock = 100

for i,j in pizzas.items():
    print(i + ": " + str(j))
ptype = input("What pizza do you want? ").lower()

if ptype in pizzas:
    quant = int(input("How many pizzas do you want? "))
    if quant > stock:
        print("Not in stock")
    else:
        cost = quant * pizzas[ptype]
        print("The cost is: " + str(cost))
else:
    print("Pizza not found")