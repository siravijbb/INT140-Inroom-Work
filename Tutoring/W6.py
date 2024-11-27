# def getUnknow(input: int):
#     for i in range(2, ((int(abs(input))))):
#         for j in range(1, 13):
#             print(F"{i} * {j} = {i*j}")

def getUnknow(input: int):
    for i in range(2, input+1):
        plusmem = 1
        for j in range(0,13):
            if j != 0:
                plusmem = i * plusmem
                print(F"{i} ** {j} =", plusmem)
            else:
                print(F"{i} ** {j} =", 1)





getUnknow(19)