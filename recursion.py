#w12 recursion
#031 ภูมิรพี ดำรงค์มงคลกุล
#048 สิรวิชญ์ แพร่วศวกิจ
#065 คณิติ หัสนีย์

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


# x^n = x * x * x * ... (n numbers of x)
# x^n = x * x^(n-1) ; x^0 = 1 [recursive definition]
def exponential(x, n):
    if n <= 1:
        return n
    return x * (x ** n - 1) * exponential(x,n-1)


def fibonacci_sum(n):
    if n <= 1:
        return n
    return fibonacci_sum(n - 1) + fibonacci_sum(n - 2)


print(fibonacci_sum(5, 3))
