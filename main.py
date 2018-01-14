from graph_pack import graph, adjacency_list
from PyQt4 import QtGui
import design
import sys

"""This is the main program. If you want to execute the program, this is the file you
will be wanting to execute. The methods and functions are going to be executed in here.
"""

city = ["", "Araguari", "Ituiutaba", "Centralina", "Itumbiara", "Capinópolis", "Monte Alegre de Minas",
         "Douradinhos", "Tupaciguara", "Uberlândia", "Indianópolis", "Nova Ponte", "Romaria",
         "Estrela do Sul", "Grupiara", "Cascalho Rico "]
city.sort()


class DijkstraApp(QtGui.QMainWindow, design.Ui_MainWindow):
    """Class representing a app."""

    def __init__(self, my_graph):
        super(self.__class__, self).__init__()
        # Graph configuration
        self.my_graph = my_graph
        self.cities_list = self.my_graph.getCitiesList()
        # UI configuration
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.search_route)
        self.cboxOrigin.addItems(my_graph.getCitiesList())
        self.cboxDestiny.addItems(my_graph.getCitiesList())


    def search_route(self):
        """Searches the route between origin and destiny."""
        origin = self.cboxOrigin.currentText()      # Gets the origin city at the GUI
        destiny = self.cboxDestiny.currentText()    # Gets the destiny city at the GUI
        route = graph.dijkstra()                    # Ajd list with the cities in route
        route_message = route.strRoute()            # Returns a string describing the route
        self.txtMessage.setPlainText(route_message) # Writes out the message
        # self.txtMessage.setPlainText("Origin: " + origin + "\n Destiny: " + destiny)
        # self.txtMessage.setPlainText(self.my_graph.getCitiesList())


def create_graph():
    """Creates and return the graph and sets edges between the cities."""
    my_graph = graph.Graph()
    for c in city:
        my_graph.insertEnd(c)
    my_graph.setEdge("Capinópolis", "Centralina")
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
    my_graph.setEdge("Romaria",  "Nova Ponte", 28)
    my_graph.setEdge("Nova Ponte", "Indianópolis", 40)
    return my_graph


def main():
    """The main function: Creates the graph and the GUI forms."""
    my_graph = create_graph()
    app = QtGui.QApplication(sys.argv)
    form = DijkstraApp(my_graph)
    form.show()
    app.exec_()



if __name__ == "__main__":
    main()


