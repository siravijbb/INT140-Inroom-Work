def getUnknow(input: int):
    alreadyPrinted = None
    for i in range(2, ((int(abs(input))))):
        for j in range(2, ((int(abs(input))))):

            if i % j != 0 and i != j:
                if alreadyPrinted != i:
                    print(F"{i}%{j}={i%j}")
                    alreadyPrinted = i


getUnknow(7)