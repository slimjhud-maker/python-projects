def ensure_users_file():
    try:
        with open("users.txt","r") as f:
            pass
    except FileNotFoundError:
        with open("users.txt","w") as f:
            f.write("Jhud,password\n")
            f.write("Bob,bobiscool\n")
            f.write("John,1234\n")

def load_users():
    users = {}
    try:
        with open("users.txt","r") as f:
            for line in f:
                if "," in line:
                    user,pwd=line.strip().split(",",1)
                    users[user.strip()] = pwd.strip()
    except FileNotFoundError:
        pass
    return users

def save_user(username,password):
    with open("users.txt","a") as f:
        f.write(f"{username},{password}\n")

def signup():
    users=load_users()
    username=input("Choose a username: ").strip()
    if username in users:
        print("Username already exists.")
        return
    password=input("Choose a password: ").strip()
    save_user(username,password)
    print("Profile created successfully.")

def calculator():
    while True:
        print("\nGeometry Calculator")
        print("1: Area of Triangle")
        print("2: Area of Square")
        print("3: Area of Trapezium")
        print("4: Area of Kite")
        print("5: Area of Rhombus")
        print("6: Area of Parallelogram")
        print("7: Back to main menu")
        choice=input("Choose an option: ").strip()

        if choice=="1":
            base=float(input("Enter base: "))
            height=float(input("Enter height: "))
            print("Area of triangle =",0.5*base*height)
        elif choice=="2":
            side=float(input("Enter side length: "))
            print("Area of square =",side*side)
        elif choice=="3":
            a=float(input("Enter first parallel side: "))
            b=float(input("Enter second parallel side: "))
            h=float(input("Enter height: "))
            print("Area of trapezium =",0.5*(a+b)*h)
        elif choice=="4":
            d1=float(input("Enter first diagonal: "))
            d2=float(input("Enter second diagonal: "))
            print("Area of kite =",0.5*d1*d2)
        elif choice=="5":
            d1=float(input("Enter first diagonal: "))
            d2=float(input("Enter second diagonal: "))
            print("Area of rhombus =",0.5*d1*d2)
        elif choice=="6":
            base=float(input("Enter base: "))
            height=float(input("Enter height: "))
            print("Area of parallelogram =",base*height)
        elif choice=="7":
            break
        else:
            print("Invalid choice.")

def login():
    users=load_users()
    username=input("Enter username: ").strip()
    if username not in users:
        print("Not existing user.")
        return
    password=input("Enter password: ").strip()
    if users[username]==password:
        print("Successfully logged in.")
        while True:
            print("\n1: Geometry Calculator")
            print("2: Logout")
            choice=input("Choose an option: ").strip()
            if choice=="1":
                calculator()
            elif choice=="2":
                print("Logged out.")
                break
            else:
                print("Invalid choice.")
    else:
        print("Wrong password.")

def main():
    ensure_users_file()
    print("Preloaded users: Jhud/password, Bob/bobiscool, John/1234")
    while True:
        print("\n1: Sign up")
        print("2: Log in")
        print("3: Quit")
        choice=input("Choose an option: ").strip()
        if choice=="1":
            signup()
        elif choice=="2":
            login()
        elif choice=="3":
            break
        else:
            print("Invalid choice.")

main()