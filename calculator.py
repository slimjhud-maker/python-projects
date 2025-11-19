def add_num(a,b):
    sum = a + b
    return(sum)

def multiply_num(a,b):
    sum = a * b
    return(sum)

def subtract_num(a,b):
    sum = a - b
    return(sum)

def divide_num(a,b):
    sum = a / b
    return(sum)

def area_circle(a):
    sum = 3.14 * a * a
    return(sum)

def circm_circle(a):
    sum = 2 * 3.14 * a
    return(sum)

def vol_cube(a):
    sum = a * a * a
    return(sum)

def vol_cubiod(a,b,c):
    sum = a * b * c
    return(sum)

def vol_cone(a,b):
    sum = 3.14 * a * a * b / 3
    return(sum)

def vol_cylinder(a,b):
    sum = a * 3.14 * a * b
    return(sum)



def main():
    print("Welcome to the calculator")
    while(True):
        choice = input("\n1: Add\n2: subtract\n3: multiply\n4: divide\n5: area of a circle\n6: circumfrence of a circle\n7: volume of a cube\n8: volume of a cubiod\n9: volume of a cone\n10: volume of a cylinder\n11: exit\n(note: scroll upwards to see your answer if you have just done a calculation)\n")
        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(add_num(num1, num2))
        
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(subtract_num(num1, num2))
        
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(multiply_num(num1, num2))
        
        elif choice == "4":
            num1 = float(input("Enter the numerator: "))
            num2 = float(input("Enter the denominator: "))
            print(divide_num(num1, num2))

        elif choice == "5":
            num1 = float(input("Enter the radius of the circle: "))
            print(area_circle(num1))

        elif choice == "6":
            num1 = float(input("Enter the radius of the circle: "))
            print(circm_circle(num1))

        elif choice == "7":
            num1 = float(input("Enter one of the side lengths of the cube: "))
            print(vol_cube(num1))

        elif choice == "8":
            num1 = float(input("Enter the width of the cuboid: "))
            num2 = float(input("Enter the length of the cuboid: "))
            num3 = float(input("Enter the height of the cuboid: "))
            print(vol_cubiod(num1,num2,num3))

        elif choice == "9":
            num1 = float(input("Enter the radius of the cone: "))
            num2 = float(input("Enter the height of the cone: "))
            print(vol_cone(num1,num2))

        elif choice == "10":
            num1 = float(input("Enter the radius of the cylinder: "))
            num2 = float(input("Enter the height of the cylinder: "))
            print(vol_cylinder(num1,num2))
            

        elif choice == "11":
            print("Exiting...")
            break


        else:
            print("Invalid input")


main()