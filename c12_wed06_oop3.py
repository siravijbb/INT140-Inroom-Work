# c12_wed00_oop2.py
#045 Saroch Pimnoi
#046 Sahaphap Yaisun
#048 Siravij Praevisavakij
#059 Korawit Rungthampaisan


class Student:
    _next_id = 67013050000  # class variable

    # constructor(firstname, lastname) -> Student
    def __init__(self, firstname: str, lastname: str):
        self._id = Student._next_id   # instance variable
        Student._next_id += 1
        self._firstname = firstname   # instance variable
        self._lastname = lastname   # instance variable

    def __str__(self):
        return f"Student({self._id}, {self._firstname}, {self._lastname})"

    def get_id(self):
        return self._id

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    @classmethod  # decorator
    def get_next_id(cls):
        return cls._next_id

    @staticmethod
    def compare(first_student, second_student):
        return first_student._id - second_student._id

    def compare_to(self, other):
        return self._id - other._id

    @classmethod
    def reset_next_id(cls, reset_value):
        cls._next_id = reset_value

    def set_firstname(self, new_firstname):
        self._firstname = new_firstname

def main():
    s0 = Student("Somchai", "Klahan")
    s1 = Student("Somsri", "Klahan")
    print(s0)
    s0.set_firstname("Somsak")
    print(s0)

    print(s1.get_next_id())
    print(s0.get_next_id())
    print("-------------------")
    Student.reset_next_id(68013050000)
    print(s1.get_next_id())
    print(s0.get_next_id())
    print(Student.get_next_id())

    print(Student.compare(s0,s1))
    print(s0.compare_to(s1))

    print(s1.get_firstname())
    print(s1.get_lastname())


def compute(f, a, b):
    return f(a,b)

def addition(x, y):
    return x + y

def multiplication(x, y):
    return x * y

ls = [addition, multiplication]

for i in ls:
    print(compute(i, 40, 70))

z = lambda i, j, k : k(i,j)   # anonymous function


print("---------------")
print( z(40,70, addition) )


print (compute ( lambda x, y : x / y  , 200, 25))