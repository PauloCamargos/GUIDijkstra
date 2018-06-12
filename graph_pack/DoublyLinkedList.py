class DLinkedList:
    """Class representing a doubly link list."""

    def __init__(self):
        pass

    def insertEnd(self):
        new_node = NodeAdjacency(city_data=city)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = self.tail.next_node

    def insertBeing(self):
        pass

    def removeNode(self, value):
        pass

    def printData(self):
        pass

    def sortList(self):
        pass
