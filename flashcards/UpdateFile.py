import Card

def update(cards, filename):
    """
    * Purpose: updates the given file with the info of the given list
    * Arguments: a 2d list with a card in 0 and a bool in 1 representing if the
    *            card is marked, the name of a file to be edited
    * Returns: nothing
    * Effects: updates the given file
    * Notes: none
    """
    string = ""
    for card in cards:
        string += card[0].front + "\n"
        string += card[0].fHint + "\n"
        string += card[0].back + "\n"
        string += card[0].bHint + "\n"
        if card[1]:
            string += "T\n"
        else:
            string += "F\n"
    file = open(filename, "w")
    file.write(string)
    file.close()
