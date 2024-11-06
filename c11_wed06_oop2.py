#c11_wed06
#045 Saroch Pimnoi
#046 Sahaphap Yaisun
#048 Siravij Praevisavakij
#059 Korawit Rungthampaisan

# fields: eid: int, name: str, salary: float
# methods: get_eid(), get_name(), get_salary(),
#    set_name(new_name), set_salary(new_salary),
#    constructor(eid, name, salary)
#    representation: Employee(eid: ..., name: ..., salary: ...)
#
# sample code to use the class
#
# special points:
#   method: compare(another_employee)
#      return -1 if this employee.eid < another_employee.eid
#      return 0 if the two employees have the same eid
#      return 1 if this employee.eid > another_employee.eid


class Employee:
    def __init__(self,eid: int,name: str,salary: float):
        self._eid = eid
        self._name = name
        self._salary = salary


    @property
    def content(self):
        return (self._eid,self._name,self._salary)

    def __repr__(self) -> str:
        return f"employee ID:{self._eid} With Name {self._name} With Salary {self._salary}"

    def get_eid(self):
        return self._eid

    def get_name(self):
        return self._name

    def get_salary(self):
        return self._salary

    def set_name(self,name:str):
        self._name = name

    def set_salary(self, salary:float):
        self._salary = salary

    def compare(self, b):
        if self._eid < b._eid:
            return -1
        elif self._eid == b._eid:
            return 0
        elif self._eid > b._eid:
            return  1



s = Employee(123,"asdfe",233)
r = Employee(222,"eerr",2345)
print(s.content)
print(s.__repr__())
print(s.get_name())
print(s.get_eid())
print(s.get_salary())
s.set_name("ooll")
s.set_salary(20000)
print(s.content)
print(s.compare(r))
