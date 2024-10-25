

# GroupName in LEB2: c09_wed11
# FileName: c09_wed11_students2.py
# member list in the file
#045 Saroch Pimnoi
#046 Sahaphap Yaisun
#048 Siravij Preavisavakij
#059 Korawit Rungthampaisan

studentsDict = {}
studentsList = []
studentsDictNumber = 1


def main():
    global studentsDictNumber  # make it global so changes inside the loop persist
    while True:
        askWantToAddtolist = input("Do you want to append a student? Type 'Yes': ")
        if askWantToAddtolist.lower() == 'yes':
            id, name, lastname = read_one_student()
            add_student_to_dict(studentsDict, id, name, lastname)
            add_student_to_lists(studentsList, id, name, lastname)
            print_students_from_list(studentsList)
            print_students_from_dict(studentsDict)
            studentsDictNumber += 1  # increment the counter properly
        else:
            break


def read_one_student() -> (int, str, str):
    while True:
        studentsID = input("Please Enter Students ID (should start with 67130500XXX): ")
        if studentsID.startswith('67130500') and len(studentsID) == 11:
            studentsID = int(studentsID)
            break
        else:
            print("Invalid ID format.")

    name = input("Please Enter First Name: ")
    lastName = input("Please Enter  Last Name: ")

    return studentsID, name, lastName


def add_student_to_dict(students: dict, id: int, name: str, lastname: str):
    global studentsDictNumber
    students[f"id{studentsDictNumber}"] = {"id": id, "name": name, "lastname": lastname}


def add_student_to_lists(students: list, id: int, name: str, lastname: str):
    students.append({"id": id, "name": name, "lastname": lastname})


def print_students_from_dict(students):  # print each student in students dict
    print("\nStudents Dictionary:")
    for key, value in students.items():
        print(f"{key}: {value}")


def print_students_from_list(students):  # print each student in the list
    print("\nStudents List:")
    for student in students:
        print(student)


main()
