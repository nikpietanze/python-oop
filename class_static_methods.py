class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}.{last.lower()}@bigwigco.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Joe', 'Montana', 60000)

import datetime
my_date = datetime.date(2019, 7, 11)

print(Employee.is_workday(my_date))

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Sarah-Smith-90000'
# emp_str_3 = 'Ralph-Tornado-40000'

# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_2.email)
# print(new_emp_2.pay)
