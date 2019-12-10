from graph2 import Graph2
import pydot

class Control:

    def __init__(self) :
        self.option = 0
        self.graph = Graph2()

    def askForGraphType(self) :
        str_opt = input("Enter a number:")
        self.option = int(str_opt)

    def drawCombinationOfGraph(self) :
        if self.option == 0:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 1:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafModulu()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 2:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 3:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 4:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 5:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 6:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
        elif self.option == 7:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.drawGrafFunkcjaPlik()
            self.graph.graph1.write_png("graf.png")
        else:
            print("No valid option!")
