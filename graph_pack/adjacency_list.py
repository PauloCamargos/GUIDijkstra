class AdjacencyList:
    """Class representing a adjacency list"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def strRout(self):
        route_message = "The shortest distance between " + self.head.data + " and " + self.tail.data + " is: "
        pass