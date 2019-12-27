# Python Object Oriented Programming
# Date: 12/27/19
# Keep at it


class Employee:
    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Seth', 'Bergman', 70000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email)
print(emp_1.fullname())
