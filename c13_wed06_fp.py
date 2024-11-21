"""
group id: c13_wed00
file: c13_wed00_fp.py
# c13_wed06_fp functional programming
deadline: sun 17 nov before midnight (23:59)


#045 Saroch
#046 Sahaphap
#048 Siravij
#059 korawit


create Employee class: _eid, _name, _salary
with methods:
getter/setter on eid, name, salary

store at least 6 employees in a list
f1: write a function to filter employee with salary > 1000
f2: write a function to map list of employees to list of employee names
f3: write a function to compute the average salary of all employee in the list
f1-f3 use functional style
generalize f1-f3 so that the function can be parameterize
"""

from functools import reduce
from typing import List

class Employee:
    def __init__(self, eid: int, name: str, salary: int):
        self._eid = eid
        self._name = name
        self._salary = salary

    def __repr__(self):
        return f"Employee(id:{self._eid}, {self._name}, {self._salary})"

    def get_id(self):
        return self._eid

    def set_id(self, _eid):
        self._eid = _eid

    def get_name(self):
        return self._name

    def set_name(self):
        self._name = _name

    def get_salary(self):
        return  self._salary

    def set_salary(self):
        self._name = _salary


emp1 = Employee(101, "Alice Green", 12350)
emp2 = Employee(102, "Bob Carter", 200)
emp3 = Employee(103, "Charlie Harris", 33120)
emp4 = Employee(104, "Diana Smith", 27560)
emp5 = Employee(105, "Edward Johnson", 50940)
emp6 = Employee(106, "Fiona Lee", 899)
emp7 = Employee(107, "George Clark", 62310)
emp8 = Employee(108, "Hannah Davis", 39050)
emp9 = Employee(109, "Ian Turner", 500)
emp10 = Employee(110, "Julia Adams", 55780)

Employees = [
    emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10
]

def filter_employees_by_salary(employees: List[Employee],  filterFunc):
    return list(filter(filterFunc, employees))

print(filter_employees_by_salary(Employees,lambda x: x.get_salary() > 1000))

def map_employees_to_names(employees: List, mapfunc):
    return list(map(mapfunc, employees))


print(map_employees_to_names(Employees, lambda x: x.get_name() ))


"""def average_salary(employees: List[Employee]):
    total_salary = reduce(lambda acc, emp:  + emp.salary, employees, 0)
    return total_salary / len(employees) if employees else 0"""




"""# f2: Map list of employees to list of employee names
employee_names = map_employees_to_names(Employees)
print("\nList of employee names:")
print(employee_names)

# f3: Compute the average salary of all employees
avg_salary = average_salary(Employees)
print(f"\nAverage salary of employees: ${avg_salary:.2f}")"""