import math


def checkMaxinClass(input: list):
    maxNum = input[0]
    for i in input:
        if input[i] > maxNum:
            maxNum = input[i]
    return maxNum


def findCnonSqure(A: float, B: float):
    Csquare = A ** 2 + B ** 2
    Cnonsquare = math.sqrt(Csquare)
    return Cnonsquare


def checkSecondMaxinClass(input: list):
    maxNum = None
    secondMaxnum = None
    for i in input:
        if maxNum == i:
            continue
        if maxNum is None or i > maxNum:
            secondMaxnum = maxNum
            maxNum = i
        elif secondMaxnum is None or i > secondMaxnum:
            secondMaxnum = i
    return secondMaxnum


print(checkSecondMaxinClass([78, 4, 3, 4, 5, 78]))


def BoolFunction(input: int):
    if input == 2:
        return True
def checkisTrue(list:list):
    for i in list:
        if BoolFunction(i) is True:
            return i



