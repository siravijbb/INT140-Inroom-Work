list = ['0', '9', '1', '2', '3', '4', '1', '1']


def findvalue(ls, value):
    foundlist = []
    for i in range(len(ls)):
        if ls[int(i)] == value:
            foundlist.append(i)
    return foundlist


print(findvalue(list, "1"))
