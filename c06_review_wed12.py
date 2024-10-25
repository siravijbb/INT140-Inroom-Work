

def km_to_mile(km):
    if type(km) is not float and not int:
        raise TypeError("wrong type")
    if km < 0:
        raise ValueError("Must be more than zero")
    return km * 0.621371192


"""write a function to check if the input parameter has dxt to each otheruplicate characters ne
- allow only str as input parameter
- raise TypeError if input validation fails
- return bool: True/False
- use while/for loop"""
def consecutive_char(msg: str):
    if not isinstance(msg, str):
        raise TypeError("Input must be a string.")
    for i in range(len(msg) - 1):
        if msg[i] == msg[i + 1]:
            return True
    return False


"""write a function to check if the input parameter has duplicate characters
- allow only str as input parameter
- raise ValueError if input validation fails
- return bool: True/False
- use nested while/for loop"""
def duplicate(msg):
    pass
    if not isinstance(msg,str):
        raise TypeError
    i = 0
    for i in range(len(msg)):
        if msg[i] == msg[i - 1]:
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
def max_value(x: int, y: int, z: int):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        raise TypeError("All inputs must be integers.")
    max_val = x
    if y > max_val:
        max_val = y
    if z > max_val:
        max_val = z
    return max_val
