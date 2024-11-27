i = 1
TotalInteresg = 0
getUserMoney = int(input("Money"))
while i < 11:
    interestRate = float(input(F"year {i} :interest rate"))
    print("interest rate:",interestRate)
    TotalInteresg = (interestRate / 100) * getUserMoney + TotalInteresg
    print("Total interest",TotalInteresg)
    calInterestRate = (interestRate / 100) * getUserMoney + getUserMoney
    print("Total Balance ",calInterestRate)
    getUserMoney = calInterestRate
    i += 1

#
# def CalInterestRateDefinedYear(Money,Year):
#     if Year <= 0:
#         return Money
#     interestRate = 2.5
#     print("interest rate:", interestRate)
#     Money = (interestRate / 100) * Money + Money
#     print("Total Balance ", Money)
#     CalInterestRateDefinedYear(Money,Year-1)
#
#
# CalInterestRateDefinedYear(100,10)