class Node:

    def __init__(self, aValue = None, aNext = None):
        self.value = aValue
        self.next = aNext

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if other == None:
            return False
        if self.value == other.value:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
