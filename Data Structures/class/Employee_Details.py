
l = list(map(int,input().split(",")))
print(l)

class Employee:
    def __init__(self):
        self.emp_id=input("Enter Employee ID")
        self.emp_name=input("Enter Employee Name")
        self.emp_salary=int(input("Enter Employee Salary"))
        self.emp_dep=input("Enter Employee department")
        
    def salary(self,salary):
        hours_worked = int(input("Enter no.of Hours worked"))
        overtime = hours_worked - 50
        if hours_worked>50:
            overtime_amount = overtime * (salary/50)
            self.emp_salary += overtime_amount
        print("salary=",self.emp_salary)
                           
    def dept_assign(self,emp_dep):
        assign = input("Enter department to be assigned")
        self.emp_dep = assign
        print("Department assigned Successfully!")

    def details(self):
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.emp_name)
        print("Employee Salary:",self.emp_salary)
        print("Employee Department:",self.emp_dep)

user1 = Employee()

            
            
        
        
