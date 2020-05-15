import sys

def main():
    if len(sys.argv) < 3:
        print("decodeFile.py requires an input file and an output file to be " +
        "specified.")
        exit()
    infile = open(sys.argv[1])

    keyTotals = []
    for i in range(0, 26):
        keyTotals.append(0)

    for shift in range(0, 26):
        for line in infile:
            for word in line.split():
                keyTotals[shift] += keyWord(shiftWord(word, shift))
        infile.seek(0)

    infile.close()
    decode(sys.argv[1], sys.argv[2], maxNumIndex(keyTotals))



#determines if a letter is uppercase
def isUppercase(letter):
    if ord(letter) <= 90 and ord(letter) >= 65:
        return True
    return False

#shifts the letter the given amount
def shiftLetter(letter, shift):
    if isUppercase(letter):
        if (ord(letter) - ord('A')) - shift < 0:
            return chr(ord(letter) + (26 - shift))
        return chr(ord(letter) - shift)
    else:
        if (ord(letter) - ord('a')) - shift < 0:
            return chr(ord(letter) + (26 - shift))
        return chr((ord(letter) - shift))

#shifts the word the given amount
def shiftWord(word, shift):
    newWord = ""
    for letter in word:
        newWord += shiftLetter(letter, shift)
    return newWord

#determines if a word is a key word
def keyWord(word):
    word = word.lower()
    if word == "i" or word == "if" or word == "a" or word == "or":
        return 1
    elif word == "it" or word == "the" or word == "be" or word == "to":
        return 1
    elif word == "of" or word == "and" or word == "in" or word == "you":
        return 1
    elif word == "are" or word == "am" or word == "that" or word == "have":
        return 1
    elif word == "for" or word == "not" or word == "on" or word == "with":
        return 1
    return 0

#decodes the file
def decode(infileName, outfileName, shift):
    infile = open(infileName)
    outfile = open(outfileName, "w")
    newFile = ""
    for word in infile:
        for letter in word:
            if isLetter(letter):
                newFile += shiftLetter(letter, shift)
            else:
                newFile += letter
    outfile.write(newFile)
    outfile.close()
    infile.close()

#finds the max num index in a list of ints
def maxNumIndex(list):
    maxIndex = 0
    for index in range(1, 26):
        if list[index] > list[maxIndex]:
            maxIndex = index
    return maxIndex

#determines if the char is a letter
def isLetter(letter):
    if ord(letter) <= ord('Z') and ord(letter) >= ord('A'):
        return True
    if ord(letter) <= ord('z') and ord(letter) >= ord('a'):
        return True
    return False

main()
