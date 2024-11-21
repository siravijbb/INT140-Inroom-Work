"""
group id: c12_wed00
filename: c12_wed00_student_class.py

Change the following application to use OOP approach

Student Information System
* this application interact with users to store and retrieve student information
  -- the user can add student info (id, firstname, and lastname) into the database
  -- the user can search for student info in the database using student id
  -- the user can list all student info from the database
* the main function:
  -- create the database and call the main user interface
* the user interface functions:
  -- interact with the users
  -- know nothing about the data format, the data structure, and the database
* the business logic functions:
  -- do not interact with the users
  -- handle all the data format, the data structure, and database
"""

def main():
    """
    create a student information database
    and start the user interface to interact with the user
    """
    db = bl_create_student_db()
    ui_main_menu(db)


"""
* the user interface functions (ui):
  ** interact with the users
  ** know nothing about the format and the structure of the data
  there are 7 ui functions:
  -- ui_main_menu(db) is the main loop to interact with the user
  -- ui_input_student_id() reads the student id from the user input
  -- ui_input_new_student_id(db) reads the student id (not in the database) from the user input
  -- ui_input_student_name(name) reads the student name (firstname or lastname) from the user input
  -- ui_add_student(db) reads student info from the user input and add it to the database
  -- ui_search_student(db) searches for student info from the database using student id for the user
  -- ui_list_students(db) lists all student info from the database for the user
"""


def ui_main_menu(db):
    """
    the main loop to interact with the user
    :param db: the student database
    """
    while True:
        print("\nStudent Information System")
        print("  [1] Add a student into the database.")
        print("  [2] Search for a student by id.")
        print("  [3] List all students.")
        result = input("  Choose one [1|2|3] or anything else to exit: ")
        try:
            match int(result):
                case 1: ui_add_student(db)
                case 2: ui_search_student(db)
                case 3: ui_list_students(db)
                case _: break
        except:
            break
    print("\nExit program normally.")


def ui_input_student_id() -> int:
    """
    interact with the user to read a student id from the user
    loop until the user inputs a valid id
    :return: a valid student id
    :raise ValueError: if the user just pressing Enter (to abort)
    """
    while True:
        value = input("  Please type a valid student id and press Enter\n"
                    "  (or just press Enter to abort): ")
        if value == "":
            raise ValueError
        sid = bl_transform_to_sid(value)
        if sid is not None:
            return sid
        print("  invalid student id format")  # if sid is None (value is invalid)


def ui_input_new_student_id(db) -> int:
    """
    interact with the user to read a student id from the user
    loop until the user inputs a valid id that is not in the database
    :return: a valid student id that is not the database
    :raise ValueError: if the user just pressing Enter (to abort)
    """
    while True:
        sid = ui_input_student_id()
        if bl_get_student(db, sid) is None:
            return sid
        print("  this student id has already existed")


def ui_input_student_name(name: str) -> str:
    """
    interact with the user to read a student name (firstname or lastname)
    loop until the user inputs a valid name format (containing no whitespace)
    :return: student name (firstname or lastname)
    """
    while True:
        value = input(f"  Please type the student {name} and press Enter\n"
                    "  (or just press Enter to abort): ")
        if value == "":
            raise ValueError
        if bl_validate_name(value):
            return value
        print("  invalid student name format (whitespace is not allowed)")


def ui_add_student(db):
    """
    interact with the user to read student id, firstname, and lastname
    and add it to the database
    :param db: the student database
    """
    print("Adding a student into the database:")
    try:
        sid = ui_input_new_student_id(db)
        firstname = ui_input_student_name("firstname")
        lastname = ui_input_student_name("lastname")
        bl_add_student(db, sid, firstname, lastname)
        print(f"Student[{sid}: {firstname} {lastname}] is added into the database successfully.")
    except ValueError:
        print("  -- No student is added --")


def ui_search_student(db):
    """
    interact with the user to read a student id from the user,
    search for that student and show it to the user
    :param db: the student database
    """
    print("Searching for a student by student id:")
    try:
        sid = ui_input_student_id()
        name = bl_get_student(db, sid)
        if name is None:
            print("  student not found")
        else:
            print(f"  student id: {sid}, firstname: {name[0]}, lastname: {name[1]}")
    except ValueError:
        print("  -- No student to be searched --")


def ui_list_students(db):
    """
    interact with the user
    to list all student info from the database
    and show it to the user
    :param db: the student database
    """
    sids = bl_get_all_student_ids(db)
    if len(sids) == 0:
        print("  -- No students in the database. --")
    for sid in sids:
        firstname, lastname = bl_get_student(db, sid)
        print(f"  student id: {sid}, firstname: {firstname}, lastname: {lastname}")


"""
* the business logic functions:
  ** business logic functions do not interact with the users
  ** business logic functions handle all data format, data structure, and database
  there are 6 business logic functions:
  -- bl_transform_to_sid(sid) for transforming sid to a valid student id if possible
  -- bl_validate_name(name) for validating student firstname and lastname
  -- bl_create_student_db() for creating/initializing the database
  -- bl_add_student(db, sid, firstname, lastname) for adding a student into the database
  -- bl_get_student(db, sid) for getting the student firstname and lastname by student id
  -- bl_get_all_student_ids(db) for getting all student ids
"""


def bl_transform_to_sid(sid: int | str) -> int | None:
    """
    transform sid (maybe int or str) to a valid student id (int) if possible
    valid student id: 67013050000 <= sid <= 67013050999
    :param sid: student id (maybe str or int)
    :return: valid student id (int) if possible; otherwise None
    """
    try:
        value = int(sid)
        if 67013050000 <= (value := int(sid)) <= 67013050999:
            return value
    except:
        pass  # fail to convert sid to an int
    return None


def bl_validate_name(name: str) -> bool:
    """
    validate student name (i.e., firstname and lastname)
    must be a string not containing any whitespace (' ', '\t', '\n')
    :param name: student firstname or lastname
    :return: True if valid; otherwise False
    """
    if type(name) is not str or ' ' in name or '\t' in name or '\n' in name:
        return False
    return True


def bl_create_student_db() -> dict:
    """
    create a student database for storing student info
    by using a dictionary as the database
    where the key is the student id (sid)
    and the value is the tuple of student firstname and lastname
    :return: the student database
    """
    return {}


def bl_add_student(db: dict[int,tuple[str,str]], sid: int, firstname: str, lastname: str) -> None:
    """
    add the student (sid, firstname, lastname) to the database
    the caller must validate sid, firstname, and lastname before calling this function
    otherwise the database may contain unexpected data
    :param db: the student database
    :param sid: the student id
    :param firstname: the student firstname
    :param lastname: the student lastname
    """
    db[sid] = firstname,lastname


def bl_get_student(db: dict[int,tuple[str,str]], sid: int) -> tuple[str,str] | None:
    """
    retrieving the student firstname and lastname from the database using the student id
    the input parameters must be valid/validated before calling this function
    :param db: the student database
    :param sid: the student id
    :return: the student firstname and lastname if found; otherwise None
    """
    return db.get(sid)


def bl_get_all_student_ids(db: dict[int,tuple[str,str]]) -> list[int]:
    """
    get a list of all student ids from the database
    :param db: the student database
    :return: the list of all student ids
    """
    return list(db.keys())


if __name__ == "__main__":
    main()