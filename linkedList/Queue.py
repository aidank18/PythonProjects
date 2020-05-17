from LinkedList import *

class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def __str__(self):
        return str(self.queue)

    def front(self):
        return self.queue.first()

    def deQueue(self):
        return self.queue.removeHead()

    def enQueue(self, item):
        if not isinstance(item, Node):
            item = Node(item, None)
        self.queue.appendItem(item)


    def size(self):
        return self.queue.size()

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False


def main():
    myQ = Queue()
    myQ.enQueue(7)
    print(myQ)
    myQ.enQueue("hi")
    myQ.enQueue(3.6)
    myQ.enQueue(56)
    print(myQ)
    assert(myQ.isEmpty() == False)
if __name__ == "__main__":
    main()
