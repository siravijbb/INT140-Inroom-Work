class Car:
    def __init__(self, regisNo, regisLocation, minIn, hourIn):  ## Number time is (1244)
        if regisNo or regisLocation is not int:
            raise TypeError("One of Args need to be number")
        if regisLocation > 76:
            raise ValueError("Is not range of Province")
        if minIn > 60 | minIn < 0:
            raise ValueError("Value Under/Over than time")
        if hourIn > 24 | hourIn < 0:
            raise ValueError("Hour: Under/over")

        self.regisNo = regisNo
        self.regisLocation = regisLocation
        self.minIn = minIn
        self.hourIn = hourIn
        self.minOut = None
        self.hourOut = None

    def __repr__(self):
        return f"Car No.{self.regisNo} Regis Location {self.regisLocation} Enter at {self.hourIn}:{self.minIn} Leave {self.minOut}:{self.minOut}  "

    def setTimeLeave(self, hourOut, minOut):
        if (hourOut < 0 or hourOut > 24):
            raise ValueError("over or under hour")
        if (minOut < 0 or minOut > 60):
            raise ValueError("over or under min")
        self.minOut = minOut
        self.hourOut = hourOut
        return 0
    def setHourIn(self,hourIn):
        if (hourIn < 0 or hourIn > 24):
            raise ValueError("over or under hour")
        self.hourOut = hourIn
        return 0

    def setMinIn(self, minIn):
        if (minIn < 0 or minIn > 60):
            raise ValueError("over or under min")
        self.minOut = minIn
        return 0


        # if((hourOut < self.hourIn) | (self.hourIn == hourOut and minOut < self.minIn)):
        #     self.hourIn = 0
        #     self.minIn = 0
        #     self.hourOut = 24
        #     self.minOut = 24


def main():
    print("Welcome to Car parking system: type 1 to enter to building or 2 to leave car")
    user_select = input()
    user_select = int(user_select)
    if user_select == 1:
        print("1 selected")
        #Call Function Add of Object
    if user_select == 2:
        passvi
    else:
        return 0




main()