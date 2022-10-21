class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(annual_salary)
        self.bonus = 5000

    def give_raise(self):
        """Add $5000 to the annual salary"""
        pay = self.salary + self.bonus
        return pay
        print(f"Your annual salary is ${self.salary} but your take home is ${pay}")

