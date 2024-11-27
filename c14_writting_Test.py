class Item:
    _keys = set()
    def __init__(self, key:str, name:str, number:int):
        if key in str.Rec: raise KeyError
        self.key = key
        self.name = name
        self.number = number

    def __str__(self):
        return f"Record(key:", self.key, "name", self.name, "number", self.number

    def __repr__(self):
        return "This is an Item, where key:", self.key, "name", self.name, "number", self.number

    def getKey(self):
        return self.key

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def setKey(self,input):
        self.key = input

    def setName(self, input):
        self.name = input

    def setNumber(self, input: int):
        self.number = input

    @staticmethod
    def validate_number(number):
        return number >= 0


