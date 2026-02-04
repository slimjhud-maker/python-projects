class Student:
    def __init__(self, student_id, name, math, science, computer):
        self.student_id = student_id
        self.name = name
        self.math = math
        self.science = science
        self.computer = computer

    def __del__(self):
        print("The destructor was called to clean the RAM")

    def calculate_total(self):
        return self.math + self.science + self.computer

    def calculate_average(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        elif avg >= 0:
            return "F"

    def display_report(self):
        total = self.calculate_total()
        avg = self.calculate_average()
        grade = self.calculate_grade()
        report = f"""
----- Student Report -----
ID       : {self.student_id}
Name     : {self.name}
Math     : {self.math}
Science  : {self.science}
Computer : {self.computer}
Total    : {total}
Average  : {avg:.2f}
Grade    : {grade}
--------------------------
"""
        print(report)


jhud = Student(123456, "Jhud", 85, 78, 92)
jhud.display_report()
print("Total:", jhud.calculate_total())
print("Average:", jhud.calculate_average())
print("Grade:", jhud.calculate_grade())