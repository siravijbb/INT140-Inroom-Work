
def fibonacci_sum(n):
    if n <= 1:
        return n
    return fibonacci_sum(n - 1) + fibonacci_sum(n - 2)

def loopfib(n):
    total = 0
    cac1 = n
    cac2 = n
    print(cac1)
    print(cac2)
    while cac1 > 1 and cac2 > 2:
        if cac1 - 1 <= 1:
            cac1 = 1
        else:
            cac1 - 1
        if cac2 - 2 <= 1:
            cac1 -= 1
        else:
            cac1 = 1

        total = cac1 + cac2 + total
    print(total)


loopfib(19)
print(fibonacci_sum(19))