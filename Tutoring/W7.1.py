
def getUnknow(input: int, base: int):
    totalDiv = 0
    while input > 1:
        input = input / base
        totalDiv += 1
    print(totalDiv)
getUnknow(1000000,2)