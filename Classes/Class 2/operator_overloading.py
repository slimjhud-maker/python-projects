class A:
    def __init__(self, x):
        self.x = x

    def f1(self):
        print("This is f1 from class A")

    def __str__(self):
        return str(self.x)
    
    def __add__(self, other):
        return A(self.x + other.x)
    
a = A(10)
a2 = A(30)
print(a + a2)