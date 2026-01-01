class Employee:
    def __init__(self, name, emp_id, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.basic_salary = basic_salary
        self.hra = 0.10 * basic_salary
        self.da = 0.05 * basic_salary
        self.tax = 0.08 * basic_salary

    def calculate_gross_salary(self):
        gross = self.basic_salary + self.hra + self.da
        print("Gross Salary:", gross)

    def calculate_net_salary(self):
        gross = self.basic_salary + self.hra + self.da
        net = gross - self.tax
        print("Net Salary:", net)

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def show_role(self):
        print("Role: Manager")


class Developer(Employee):
    def show_role(self):
        print("Role: Developer")


m = Manager("Jhud", 101, 5000)
m.display_details()
m.show_role()
m.calculate_gross_salary()
m.calculate_net_salary()