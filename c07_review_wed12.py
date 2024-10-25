#031 ภูมิรพี ดำรงค์มงคลกุล
#048 สิรวิชญ์ แพร่วศวกิจ
#065 คณิติ หัสนีย์

# c06 2024-09-25 Group Wed Solution
"""write a function to convert the input parameter from kms to miles
- allow only int or float as input parameter
- raise TypeError("Only int or float") if input parameter is a wrong type
- raise ValueError("Only Non-Negative Value") if input parameter is less than 0
- convert kms to miles and return the result"""


def km_to_mile(km):
    if not isinstance(km, (int, float)):
        raise TypeError("Only int or float")
    if km < 0:
        raise ValueError("Only Non-Negative Value")
    return km * 0.621371192


"""write a function to check if the input parameter has duplicate characters next to each other
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use while/for loop"""


def consecutive_char(msg: str):
    if type(msg) is not str:
        raise TypeError
    for i in range(len(msg) - 1):
        if msg[i] == msg[i + 1]:
            return True
    return False


"""write a function to check if the input parameter has duplicate characters
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use nested while/for loop"""


def duplicate(msg):
    if type(msg) is not str:
        raise TypeError
    length = len(msg)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if msg[i] == msg[j]:
                return True
    return False


"""write a function to find the maximum value of the three int parameters
- allow only int as input parameter
- raise TypeError if input validation fails
- return the maximum value of the three values
- use only comparison: <, >, <=, >=, !=, ==
*** focus on performance by minimizing redundant comparison 
- not allow the use of lists or any functions
- multiple parameters with the same value has no effect to the return value"""


def max_value(x, y, z):
    if x >= y:
        if x >= z:
            return x
        return z
    if y >= z:
        return y
    return z


