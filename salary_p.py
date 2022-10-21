from main import Employee

first_name = input("Enter your first name ")
last_name = input("Enter last name ")
salary = input("Enter salary ")

employee = Employee(first_name, last_name,salary)

employee.give_raise()



