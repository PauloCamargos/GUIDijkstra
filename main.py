from graph_pack import graph

"""This is the main program. If you want to execute the program, this is the file you
will be wanting to execute. The methods and functions are going to be executed in here.
"""
graph = graph.Graph()


def create_graph():
    resp = "y"
    while resp != "quit":
        city_name = input("Enter the name of the city: ")
        graph.insertEnd(city=city_name)
        resp = input("Insert another city (y/n)? ")


def set_aresta():
    city_1 = input("Enter the first city: ")
    city_2 = input("Enter the second city: ")
    graph.setEdge(city_1, city_2)

def search_path():
    origin = input("Enter the city of departure: ")
    destiny = input("Enter the city of arrival: ")
    graph.shortestDistance(origin, destiny)



create_graph()
set_aresta()


