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

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Sam', 'Smith', 50000)
emp_2 = Employee('Joe', 'Montana', 60000)

# * Call the special methods specifically
# print(repr(emp_1))
# print(str(emp_1)) # Default when True

print(len(emp_2))
