from graph_pack import node_graph


class NodeAdjacency(node_graph.NodeGraph):              # NodeGraph is a parent class
    """Class representing a node of a adjacency list. This class is a child of node_graph.NodeGraph() class."""

    # def __init__(self, city_data="", next_node=None, previous_node=None, adj_list=None):
    #     super().__init__(city_data, next_node, previous_node, adj_list)
    #     # super(self.__class__, self).__init__()

    def __init__(self, weight = 0, accumulated_weight = 1000, was_visited=False, previous_city=""):
        """Initializes the class."""
        super().__init__()
        self.weight = weight
        self.accumulated_weight = accumulated_weight
        self.was_visited = was_visited
        self.previous_city = previous_city


def main():
    # a = NodeAdjacency
    # print(isinstance(NodeAdjacency, node_graph.NodeGraph))
    # print(isinstance([], list))
    a = NodeAdjacency()
    print(isinstance(a, node_graph.NodeGraph))


if __name__ == "__main__":
    main()
