from Passenger import *
from Station import *

class MetroSim:

    def __init__(self, filename):
        self.train = {"stationIndex": 0, "occupants": []}
        self.stations = []
        self.passengerCount = 1
        infile = open(filename)
        i = 1
        for line in infile:
            self.train["occupants"].append(Queue())
            self.stations.append(Station(line[:-1], False, i, Queue()))
            i += 1
        self.stations[0].trainHere = True
        infile.close()

    def __str__(self):
        #print(self.train["occupants"][1])
        string = "Passengers on the train: {"
        temp = ""
        for station in self.train["occupants"]:
            if not station.isEmpty():
                temp += str(station)[1:-1] + ", "
        string += temp[:-2] + "}\n"
        for station in self.stations:
            string += str(station) + "\n"
        return string

    def run(self):
        quit = False
        command = ""
        while not quit:
            print(self)
            command = input()
            quit = self.__determineInput(command)


    def __determineInput(self, command):
        if command == "m m":
            self.__move()
            return False
        if command[0] == "p":
            self.__addPassenger(command)
            return False
        if command == "m f":
            return True
        if command == "de":
            for Q in self.train["occupants"]:
                print(Q)
        return False

    def __move(self):
        self.__boardPassenger()
        self.stations[self.train["stationIndex"]].trainHere = False
        self.train["stationIndex"] += 1
        if self.train["stationIndex"] >= 26:
            self.train["stationIndex"] = 0
        self.stations[self.train["stationIndex"]].trainHere = True
        self.__disembark()

    def __addPassenger(self, command):
        passenger = Passenger(self.passengerCount, int(command[2]),
        int(command[4:]))
        self.passengerCount += 1
        self.stations[int(command[2]) - 1].passengers.enQueue(passenger)

    def __boardPassenger(self):
        index = self.train["stationIndex"]
        while not self.stations[index].passengers.isEmpty():
            passenger = self.stations[index].passengers.deQueue()
            #print(passenger.value, passenger.next)
            self.train["occupants"][passenger.value.to - 1].enQueue(passenger.value)
            #print(passenger.value, passenger.next)

    def __disembark(self):
        index = self.train["stationIndex"]
        while not self.train["occupants"][index].isEmpty():
            node = self.train["occupants"][index].deQueue()
            print("Passenger " + str(node.value.name) + " left at station " +
            str(node.value.to) + ".")


mySim = MetroSim("stations.txt")
mySim.run()
