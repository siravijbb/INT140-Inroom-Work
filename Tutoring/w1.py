money = int(input("money: "))

while money > 0:
    pricer = int(input("how much per eachj"))
    if (money - pricer >= 0) and pricer > 0:
        money -= pricer
        print(F"total money left {money}")
    elif pricer <= 0:
        print("exited")
        break
    else:
        print("not enought money")


if money <= 0:
    print("no money left")

