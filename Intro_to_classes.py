# Python Object Oriented Programming


class Employee:
    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'


emp_1 = Employee('Seth', 'Bergman', 70000)

print(emp_1)

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Seth'
# emp_1.last = 'Bergman'
# emp_1.email = 'seth.bergman@gmail.com'
# emp_1.pay = 70000
#
# emp_2.first = 'Test'
# emp_2.last = 'Employee'
# emp_2.email = 'test.employee@gmail.com'
# emp_2.pay = 80000

print(emp_1.email)
