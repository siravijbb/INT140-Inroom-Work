# C12_wed00_oop2

class Student:
    next_id = 6713050000 #class varable

    #construcutor
    def __init__(self, firstname: str, lastname: str):
        self._id = Student.next_id #instance valable
        Student.next_id += 1
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"Student({self._id}, {self.firstname}, {self.lastname})"


s0 = Student("Somchai","WE")
s1 = Student("234","2343")

print(s0)
print(s1)

Student.next_id = 100
s2 = Student("2345",2345)
s0.firstname = "SOMpong"
print(s2)
s3 = Student("234",2345)
print(s3)
s3.nickname = "234"
print(s3.nickname)
print("before",s0._id)
s0.__id = 244
print("after",s0._id)

    #id:int
    #firstname: string
    #lastname :string
    #constructure(firstname, lastname)
    #get_id() -> int
    #get_firstname() -> str
    #get_lastname() -> str
    #set_firstname() -> none
    #set_lastname() -> none
