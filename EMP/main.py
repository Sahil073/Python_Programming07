# 
class Employee:
    count = 0
    def __init__(self, name, emp_id, dept, salary):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.salary = salary
        Employee.count += 1
    def display_info(self):
        st = f'''Name: {self.name}
Employee_Id: {self.emp_id}
Department: {self.dept}
Salary: {self.salary} '''
        print(st)
    def update_info(self, name=None,emp_id=None, dept=None, salary=None):
        if name:
            self.name = name
        if dept:
            self.dept = dept
        if salary:
            self.salary = salary
    def increment_salary(self, per):
        self.salary = self.salary + (self.salary * (per / 100))
        print(f'{per}% added to employee salary')  
    def number_employee(cls):
        print(f'total number of employee {cls.count}')      
# Class for System Management.....

class Employee_management(Employee):
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, emp_id, dept, salary):
        self.employees[emp_id] = Employee(name, emp_id, dept, salary)
        print(f'Employee With {emp_id} added successfully.')

    def salary_increment(self, emp_id, increment):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.increment_salary(increment)
                break
        else:
            print(f'Employee with ID {emp_id} not found.')

    def display_all(self):
        if not self.employees:
            print('No employees to display.')
        else:
            for employee in self.employees:
                self.employees[employee].display_info()
                print(('-'*100).center(20))
system = Employee_management()

print("Good morning")
print("For add employee - press 1")
print("For salary increment - press 2")
print("For display all - press 3")
print("Number of Employee - press 4")
print("For Exit - press 5")
while True:
    user_input = int(input("What you want to perfome: "))
    match user_input:
        case 1:
            name = input("Enter name: ")
            emp_id = input('Enter Employee id: ')
            depart = input("Enter department name: ")
            salar = input('Enter salary: ')
            system.add_employee(name,emp_id,depart,salar)
        case 2:
            emp_id = input("Enter emp_id: ")
            per = input("Enter percentage you want to increase: ")
            system.salary_increment(emp_id, per)
        case 3:
            print("list of all employee....")
            system.display_all()    
        case 4:
            system.number_employee()    
        case 5:
            print("thanku for using")
            break
        case _:
            print('error 404 value not find')
            print("Enter a valid input...")
    