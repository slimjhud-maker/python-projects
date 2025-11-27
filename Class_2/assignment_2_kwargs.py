def product_info(**kwargs):
    print(f"Name: {kwargs['name']}\nPrice: {kwargs['price']}\nCategory: {kwargs['category']}")

print("Assignment 2:")
product_info(name="Laptop", price=1200, category="Electronics")