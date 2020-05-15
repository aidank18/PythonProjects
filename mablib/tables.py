number = input("Factor: ")
print("n |", number, "* n")
print("----------")
i = 1
while i < 10:
    print(str(i) + " | " + str(i * int(number)))
    i += 1
