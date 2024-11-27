import math


def getUnknow(input: int):
    for i in range(2, ((int(abs(input))))):
        if input % i == 0:
            print(i)


getUnknow(10)
