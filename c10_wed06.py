# c10_wed06
# Saroch Pimnoi 044
# Sahaphap Yaisun 046
# korawit Rungthampaisan 059
# Siravij Praevisavakij 048


studentsDict = {}
studentsList = []
studentsDictNumber = 1


def main():
    global studentsDictNumber  # make it global so changes inside the loop persist
    while True:
        askWantToAddtolist = input(
            "Do you want to append a student? Type '1': \nDo you want to find a student with ID? Type '2':\n input: ")

        if askWantToAddtolist == '1':
            id, name, lastname = read_one_student()
            add_student_to_dict(studentsDict, id, name, lastname)
            add_student_to_lists(studentsList, id, name, lastname)
            print_students_from_list(studentsList)
            print_students_from_dict(studentsDict)
            studentsDictNumber += 1  # increment the counter properly

        elif askWantToAddtolist == '2':
            find_data(studentsDict)


def read_one_student() -> (str, str, str):
    while True:
        TempstudentsID = input("Please Enter Students ID (should start with 67130500XXX): ")

        if TempstudentsID.startswith('6713050') and len(TempstudentsID) == 11:
            if TempstudentsID not in [student['id'] for student in studentsDict.values()] and TempstudentsID not in [
                student['id'] for student in studentsList]:
                break
            else:
                print("Already IN")

        else:
            print("Invalid ID format.")
    studentsID = TempstudentsID
    name = input("Please Enter First Name: ")
    lastName = input("Please Enter Last Name: ")

    return studentsID, name, lastName


def add_student_to_dict(students: dict, id: str, name: str, lastname: str):
    global studentsDictNumber
    students[f"id{studentsDictNumber}"] = {"id": id, "name": name, "lastname": lastname}


def add_student_to_lists(students: list, id: str, name: str, lastname: str):
    students.append({"id": id, "name": name, "lastname": lastname})


def print_students_from_dict(students):  # print each student in the dictionary
    print("\nStudents Dictionary:")
    for key, value in students.items():
        print(f"{key}: {value}")


def print_students_from_list(students):  # print each student in the list
    print("\nStudents List:")
    for student in students:
        print(student)


def find_data(students):
    search_id = input("Enter the student ID you want to find: ")
    for key, student in students.items():
        if student['id'] == search_id:
            print(f"Found: {student}")
            return
    print("Student not found.")


main()
