def isLetter(letter):
    if ord(letter) <= ord('Z') and ord(letter) >= ord('A'):
        return True
    if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
        return True
    return False

def isUppercase(letter):
    if ord(letter) <= 90 and ord(letter) >= 65:
        return True
    return False

inFileName = input("Enter a file to encrypt: ")
outFileName = input("Enter a file to output: ")
shiftAmount = int(input("Enter a shift amount: "))
infile = open(inFileName)
outfile = open(outFileName, "w")
while shiftAmount <= -26:
    shiftAmount += 26
while shiftAmount >= 26:
    shiftAmount -= 26
newFile = ""
for word in infile:
    for letter in word:
        if isLetter(letter):
            if isUppercase(letter):
                if (ord(letter) - ord('A')) + shiftAmount >= 26:
                    newFile += chr((ord(letter) + (shiftAmount - 26)))
                else:
                    newFile += chr((ord(letter) + shiftAmount))
            else:
                if (ord(letter) - ord('a')) + shiftAmount >= 26:
                    newFile += chr((ord(letter) + (shiftAmount - 26)))
                else:
                    newFile += chr((ord(letter) + shiftAmount))
        elif letter == ' ':
            newFile += " "
        else:
            newFile += letter
outfile.write(newFile)
outfile.close()
infile.close()
