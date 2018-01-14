from graph_pack import adjacency_list, node_graph


class Graph:
    """Doubly linked list representing a graph"""

    def __init__(self, head=None, tail=None):
        """Initializes the class."""
        self.head = head  # node_graph.NodeGraph()
        self.tail = tail  # node_graph.NodeGraph()
        self.priorityList = adjacency_list.AdjacencyList()

    def printData(self):
        """Prints the data inside each node in the graph."""
        print(self.getCitiesList())
        # for c in self.getCitiesList():
        #     print("-> " + c)

    def insertEnd(self, city):
        """Inserts a node with 'city' data at the end of the list."""
        new_node = node_graph.NodeGraph(city_data=city)
        if self.head is None:                   # If the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = self.tail.next_node

    def setEdge(self, city_1, city_2, edge=0):
        """Sets the weight (distance) between both parameters."""
        pass

    def getCitiesList(self):
        """Returns a simple list containing all cities registered in the graph."""
        cities_list = []
        temp = self.head
        while temp is not None:
            cities_list.append(temp.city_data)
            temp = temp.next_node
        return cities_list

    def shortestDistance(self, origin, destiny):
        pass

    def dijkstra(self):
        pass


def main():
    my_graph = Graph()
    my_graph.insertEnd("E")
    my_graph.insertEnd("D")
    my_graph.insertEnd("C")
    my_graph.insertEnd("B")
    my_graph.insertEnd("A")
    my_graph.printData()


if __name__ == "__main__":
    main()

