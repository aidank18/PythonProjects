
isPal = True
close = False
while isPal or close:
    isPal = True
    close = False
    word = input("Enter a word: ")
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            isPal = False
            break
        if i >= 2:
            close = True
    if isPal:
        print("Its a palindrome!!")
    elif close:
        print("Its close enough!")
    else:
        print("Thank you for your time.")
