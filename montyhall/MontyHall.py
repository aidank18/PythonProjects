from random import random


def game(stay):
    doors = makeDoors()
    choice = int(random() * 3)
    for i in range(0, 2):
        if (i != choice) and doors[i] == "g":
            doors[i] = "r"
            break
    if stay:
        return doors[choice]
    else:
        doors[choice] = "r"
        for door in doors:
            if door != "r":
                return door

def makeDoors():
    doors = ["g", "g", "c"]
    for i in range(0, 10):
        val1 = int(random() * 3)
        val2 = int(random() * 3)
        temp = doors[val1]
        doors[val1] = doors[val2]
        doors[val2] = temp
    return doors


def tests(stay):
    cars = 0
    for i in range(0, 10000):
        if game(stay) == "c":
            cars += 1
    probability = cars/10000
    if stay:
        print()
        print("The probability of picking the car by staying with the same door is", probability)
        print()
    else:
        print()
        print("The probability of picking the car by switching doors is", probability)
        print()

tests(False)
