from Node import *

class LinkedList:

    def __init__(self, aStart = None):
        self.__start = aStart
        if self.__start == None:
            self.__size = 0
        else:
            self.__size = self.__traverseList(self.__start, False)

    def __str__(self):
        list = "[" + self.__traverseList(self.__start)
        list = list[:-2]
        list += "]"
        return list

    def __len__(self):
        return self.__size

    def __traverseList(self, curr, string = True):
        if curr == None:
            if string:
                return ""
            return 0
        if string:
            return str(curr.value) + ", " + self.__traverseList(curr.next)
        return 1 + self.__traverseList(curr.next, False)

    def appendItem(self, node = None, number = None):
        if node != None:
            if self.__start == None:
                self.__start = node
                self.__size += self.__traverseList(node)
                return
            self.__addNode(self.__start, node)
            self.__size += 1
        elif number != None:
            if self.__start == None:
                self.__start = Node(number, None)
                self.__size += 1
                return
            self.__addNumber(self.__start, number)
            self.__size += 1

    def __addNode(self, curr, node):
        if curr.next == None:
            curr.next = node
            return
        self.__addNode(curr.next, node)

    def __addNumber(self, curr, number):
        if curr.next == None:
            curr.next = Node(number, None)
            return
        self.__addNumber(curr.next, number)

    def prependItem(self, node = None, number = None):
        if number != None:
            node = Node(number, None)
        curr = node
        while curr.next != None:
            curr = curr.next
        curr.next = self.__start
        self.__start = node
        self.__size = self.__traverseList(node, False)


    def removeHead(self):
        if self.__start == None:
            return None
        self.__size -= 1
        temp = self.__start
        self.__start = self.__start.next
        return temp

    def removeTail(self):
        if self.__size == 0 or self.__size == 1:
            return self.removeHead()
        curr = self.__start
        while curr.next.next != None:
            curr = curr.next
        temp = curr.next
        curr.next = None
        self.__size -= 1
        return temp

    #counts the number of nodes with the specified item
    def count(self, item):
        if self.__size == 0:
            return 0
        counter = 0
        curr = self.__start
        while curr.next != None:
            if curr.value == item:
                counter += 1
            curr = curr.next
        return counter

    #returns the first index of the given item
    def index(self, item):
        if self.__size == 0:
            return None
        curr = self.__start
        ind = 0
        while curr != None:
            if curr.value == item:
                return ind
            curr = curr.next
            ind += 1
        return None

    def insert(self, index, item):
        if index > self.__size:
            return
        elif index == 0:
            self.prependItem(item)
        elif index == self.__size:
            self.appendItem(item)
        else:
            curr = self.__start
            i = 0
            while i + 1 != index:
                curr = curr.next
                i += 1
            curr.next = Node(item, curr.next)
            self.__size += 1

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def size(self):
        return self.__size

    def clear(self):
        self.__size = 0
        self.__start = None

    def first(self):
        return self.__start

    def last(self):
        if self.__size == 0:
            return None
        curr = self.__start
        while(curr.next != None):
            curr = curr.next
        return curr

    def elemAt(self, index):
        if index < 0 or index >= self.__size:
            return None
        curr = self.__start
        for i in range(0, index):
            curr = curr.next
        return curr
