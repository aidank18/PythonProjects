class Passenger:

    def __init__(self, aName = -1, astart = -1, aTo = -1):
        self.name = aName
        self.start = astart
        self.to = aTo

    def __str__(self):
        return ("[" + str(self.name) + ", " + str(self.start) + ", " +
        str(self.to) + "]")


myPassenger = Passenger()
print(myPassenger)
