class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.grade = input("Enter student grade: ")
        self.subject = input("Enter student subject: ")
    def __del__(self):
        print("Destructer was called to clean the RAM")

    def study(self):
        print("Choose a study activity:")
        print("1. Read textbook")
        print("2. Solve practice problems")
        print("3. Watch tutorial videos")
        print("4. Revise notes")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print(self.name + " is reading the " + self.subject + " textbook.")
        elif choice == "2":
            print(self.name + " is solving " + self.subject + " practice problems.")
        elif choice == "3":
            print(self.name + " is watching " + self.subject + " tutorial videos.")
        elif choice == "4":
            print(self.name + " is revising " + self.subject + " notes.")
        else:
            print("Invalid choice.")

    def introduce(self):
        print("Hi, I'm " + self.name + ", in grade " + self.grade + ", and my favorite subject is " + self.subject + ".")

student_1 = Student()
student_1.introduce()
student_1.study()

student_2 = Student()
student_2.introduce()
student_2.study()