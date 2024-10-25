# GroupName in LEB2: c08_wed02
# FileName: c08_wed02_students.py
# member list in the file
# 045 Saroch Pimnoi
# 046 Sahaphap Yaisun
# 048 Siravij Praevisavakij
# 059 Korawit Rungthampaisan



students = []

def student_data(all: list, id: int, name: str, lastname: str):
    # build a list of (id, name, lastname)
    student = [id, name, lastname]
    # append this list to all
    all.append(student)


def input_one_member(all: list):
    # read id, name, lastname from user input
    id = int(input("Enter ID: "))
    if type(id) is not int:
        raise TypeError("expected number")
    name = input("Enter name: ")
    if type(name) is not str:
        raise TypeError("Expect name")
    lastname = input("Enter lastname: ")
    if type(lastname) is not str:
        raise TypeError("expect Lastname")

    # add it to all by calling student_data
    student_data(all, id, name, lastname)


def main():
    students = []
    while True:
        input_one_member(students)
        print("students in list:",students)
        print(students[0])

main()
