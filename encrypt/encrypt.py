word = input("Enter a word or phrase to encrypt: ")
shiftAmount = input("Enter a shift amount: ")
numberShiftAmount = int(shiftAmount)
while numberShiftAmount < 0:
    numberShiftAmount += 26
while numberShiftAmount > 26:
    numberShiftAmount -= 26
newWord = ""
for ch in word:
    if ch != ' ':
        newWord += chr((ord(ch) + numberShiftAmount))
    else:
        newWord += " "
print(newWord)
