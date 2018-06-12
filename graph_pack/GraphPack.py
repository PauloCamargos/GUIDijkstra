""" Module containing classes representing a graph."""
import math

# -------------------------- GRAPH -------------------------------------------
from builtins import float


class Graph:
    """Doubly linked list representing a graph"""

    def __init__(self, head=None, tail=None):
        """Initializes the class."""
        self.head = head  # node_graph.NodeGraph()
        self.tail = tail  # node_graph.NodeGraph()
        self.priorityList = AdjacencyList()

    def printData(self):
        """Prints the data inside each node in the graph."""
        print(self.getCitiesList())
        # for c in self.getCitiesList():
        #     print("-> " + c)

    def insertEnd(self, city):
        """Inserts a node with 'city' data at the end of the list."""
        new_node = NodeGraph(city_data=city)
        if self.head is None:                   # If the list is empty
            self.head = self.tail = new_node
            print("Inserting " + city + " as first node...")
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = self.tail.next_node
            print("Inserting " + city + " at the end...")

    def setEdge(self, city_1, city_2, edge=0):
        """Sets the weight (distance) between both parameters."""
        node_1 = self.findNode(city_1)
        node_2 = self.findNode(city_2)
        if node_1 is None or node_2 is None:
            print("ERROR. TRY AGAIN!")
            return
        else:
            node_1.adj_list.insertEnd(city_2, edge)
            node_2.adj_list.insertEnd(city_1, edge)
            print("Arestas inseridas com sucesso!\n")

    def findNode(self, city):
        temp = self.head
        while temp is not None:
            if temp.city_data == city:
                print("Node with data '{}' found. Returning...".format(city))
                break
            else:
                temp = temp.next_node
        if temp is None:
            print("ERROR -> Couldn't find '{}' node. Try again.".format(city))
        return temp

    def getCitiesList(self):
        """Returns a simple list containing all cities registered in the graph."""
        cities_list = []
        temp = self.head
        while temp is not None:
            cities_list.append(temp.city_data)
            temp = temp.next_node
        return cities_list

    def printGraph(self):
        temp = self.head
        str_data = ""
        while temp is not None:
            print(temp.city_data + " -> ")
            temp_adj = temp.adj_list.head
            while temp_adj is not None:
                str_data += temp_adj.city_data + "(" + str(temp_adj.weight) + ") -> "
                print(str_data)
                temp_adj = temp_adj.next_node
            temp = temp.next_node

    def shortestDistance(self, origin, destiny):
        pass

    def dijkstra(self):
        pass


# --------------------------------- NODE GRAPH ------------------------------------------

class NodeGraph:
    """Class representing a node of the graph."""

    def __init__(self, city_data="", next_node=None, previous_node=None):
        self.city_data = city_data
        self.next_node = next_node
        self.previous_node = previous_node
        self.adj_list = AdjacencyList()


# ---------------------------------- ADJACENCY LIST --------------------------------------

class AdjacencyList:
    """Class representing a adjacency list"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insertEnd(self, city, weight=0):
        """Inserts a node with 'city' data at the end of the list."""
        new_node = NodeAdjacency(city_data=city, weight=weight)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = self.tail.next_node

    def sortList(self):
        pass

    def printData(self):
        """Prints the data inside each node in the graph."""
        print(self.getCitiesList())

    def getCitiesList(self):
        """Returns a simple list containing all cities registered in the graph."""
        cities_list = []
        temp = self.head
        while temp is not None:
            cities_list.append(temp.city_data)
            temp = temp.next_node
        return cities_list


# --------------------------------- NODE ADJACENCY -------------------------------------

class NodeAdjacency(NodeGraph):              # NodeGraph is a parent class
    """Class representing a node of a adjacency list. This class is a child of node_graph.NodeGraph() class."""

    # def __init__(self, city_data="", next_node=None, previous_node=None, adj_list=None):
    #     super().__init__(city_data, next_node, previous_node, adj_list)
    #     # super(self.__class__, self).__init__()

    def __init__(self, city_data="", next_node=None, previous_node=None, weight=0, accumulated_weight=float("inf"),
                 was_visited=False, previous_city=""):
        """Initializes the class."""
        super(NodeAdjacency, self).__init__(city_data, next_node, previous_node)
        self.weight = weight
        self.accumulated_weight = accumulated_weight
        self.was_visited = was_visited
        self.previous_city = previous_city


def main():
    city = ["Araguari", "Ituiutaba", "Centralina", "Itumbiara", "Capinópolis", "Monte Alegre de Minas",
            "Douradinhos", "Tupaciguara", "Uberlândia", "Indianópolis", "Nova Ponte", "Romaria",
            "Estrela do Sul", "Grupiara", "Cascalho Rico"]
    city.sort()

    my_graph = Graph()
    for c in city:
        my_graph.insertEnd(c)

    my_graph.setEdge("Capinópolis", "Centralina", 40)
    my_graph.setEdge("Centralina", "Ituiutaba", 30)
    my_graph.setEdge("Ituiutaba", "Monte Alegre de Minas", 85)
    my_graph.setEdge("Ituiutaba", "Douradinhos", 90)
    my_graph.setEdge("Centralina", "Itumbiara", 20)
    my_graph.setEdge("Centralina", "Monte Alegre de Minas", 75)
    my_graph.setEdge("Itumbiara", "Tupaciguara", 55)
    my_graph.setEdge("Monte Alegre de Minas", "Douradinhos", 28)
    my_graph.setEdge("Monte Alegre de Minas", "Uberlândia", 60)
    my_graph.setEdge("Monte Alegre de Minas", "Tupaciguara", 44)
    my_graph.setEdge("Douradinhos", "Uberlândia", 63)
    my_graph.setEdge("Uberlândia", "Araguari", 30)
    my_graph.setEdge("Uberlândia", "Romaria", 78)
    my_graph.setEdge("Uberlândia", "Indianópolis", 45)
    my_graph.setEdge("Uberlândia", "Tupaciguara", 60)
    my_graph.setEdge("Araguari", "Cascalho Rico", 28)
    my_graph.setEdge("Araguari", "Estrela do Sul", 34)
    my_graph.setEdge("Cascalho Rico", "Grupiara", 32)
    my_graph.setEdge("Grupiara", "Estrela do Sul", 38)
    my_graph.setEdge("Estrela do Sul", "Romaria", 27)
    my_graph.setEdge("Romaria", "Nova Ponte", 28)
    my_graph.setEdge("Nova Ponte", "Indianópolis", 40)

    # my_graph.printData()
    my_graph.printGraph()


if __name__ == "__main__":
    main()

