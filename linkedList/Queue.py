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



myQ = Queue()
print(myQ)
