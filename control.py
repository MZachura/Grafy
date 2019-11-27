from graph2 import Graph2

class Control:

    def __init__(self) :
        self.option = 0
        self.graph = Graph2()

    def askForGraphType(self) :
        str_opt = input("Enter a number:")
        self.option = int(str_opt)

    def drawCombinationOfGraph(self) :
        if self.option == 0:
            self.graph.drawGraph()
        elif self.option == 1:
            self.graph.drawGrafModulu()
        elif self.option == 2:
            self.graph.drawGrafFunkcji()
        elif self.option == 3:
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
        elif self.option == 4:
            self.graph.drawGraph()
            self.graph.drawGrafFunkcji()
        elif self.option == 5:
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
        elif self.option == 6:
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
        else:
            print("No valid option!")
