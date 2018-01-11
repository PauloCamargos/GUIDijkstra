from graph_pack import graph
from PyQt4 import QtGui
import design
import sys

"""This is the main program. If you want to execute the program, this is the file you
will be wanting to execute. The methods and functions are going to be executed in here.
"""


class DijkstraApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnSearch.clicked.connect(self.search_route)

    def search_route(self):
        self.txtMessage.setPlainText("Estou funcionando")

graph = graph.Graph()


def create_graph():
    resp = "y"
    while resp == "y":
        city_name = input("Enter the name of the city: ")
        graph.insertEnd(city=city_name)
        resp = input("Insert another city (y/n)? ")


def configure_edge():
    city_1 = input("Enter the first city: ")
    city_2 = input("Enter the second city: ")
    graph.setEdge(city_1, city_2)


def search_route():
    origin = input("Enter the city of departure: ")
    destiny = input("Enter the city of arrival: ")
    graph.shortestDistance(origin, destiny)


def main():
    print("Im here")
    app = QtGui.QApplication(sys.argv)
    form = DijkstraApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()


