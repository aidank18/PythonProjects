from Queue import *

class Station:
    def __init__(self, aName = None, aTrainHere = False, aNumber = -1, aPassengers = Queue()):
        self.name = aName
        self.trainHere = aTrainHere
        self.number = aNumber
        self.passengers = aPassengers

    def __str__(self):
        if self.trainHere:
            string = "TRAIN: "
        else:
            string = "       "
        string += "[" + str(self.number) + "] " + str(self.name) + " " + str(self.passengers)
        return string
