class Graph:
    """Describes a graph"""

    def __init__(self, begin=None, end=None, data=""):
        """Initializes the class."""
        self.begin = begin
        self.end = end
        self.data = data

    def print_data(self):
        """Prints the data inside each node in the graph."""
        print(self.data)

    def insertEnd(self, city):
        pass

    def setEdge(self, city_1, city_2):
        pass

    def shortestDistance(self, origin, destiny):
        pass

