from graph2 import Graph2
import pydot
import os

class Control:

    def __init__(self) :
        self.option = 0
        self.graph = Graph2()

    def askForGraphType(self) :
        print("0 = plikow")
        print("1 = modulu")
        print("2 = funkcji")
        print("3 = funkcja-plik")
        print("4 = plikow, modulu")
        print("5 = plikow, funkcji")
        print("6 = plikow, funkcja-plik")
        print("7 = modulu, funkcji")
        print("8 = modulu, funkcja-plik")
        print("9 = funkcja-plik, funkcji ")
        print("10 = plikow, modulow, funkcji ")
        print("11 = wszystkie")
        print("12 = Zlozonosc Cyklometryczna ")
        print("13 = Roznice miedzy commitami ")
        str_opt = input("Enter a number:")
        self.option = int(str_opt)

    def drawCombinationOfGraph(self) :
        if self.option == 0:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.graph1.write_png("graf.png")
            self.graph.graph1.write_dot("graf.dot")
            cmd = 'git log --pretty=%H -1'
            print("wersja: ")
            os.system(cmd)
        elif self.option == 1:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafModulu()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 2:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 3:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafFunkcjaPlik()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 4:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 5:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 6:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafFunkcjaPlik()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 7:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 8:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcjaPlik()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 9:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGrafFunkcjaPlik()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 10:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 11:
            self.graph.graph1 = pydot.Dot(graph_type='digraph')
            self.graph.drawGraph()
            self.graph.drawGrafModulu()
            self.graph.drawGrafFunkcji()
            self.graph.drawGrafFunkcjaPlik()
            self.graph.graph1.write_png("graf.png")
            print("wersja: ")
            cmd = 'git log --pretty=%H -1'
            os.system(cmd)
        elif self.option == 12:
            cmd = 'radon cc /Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy -s'
            os.system(cmd)
        elif self.option == 13:
            cmd = 'git log --pretty=%H -1'
            cmd1 = 'git log --pretty=%H -2'
            #os.system(cmd)
            #os.system(cmd1)
            x = os.popen(cmd).read()
            x2 = os.popen(cmd1).read()
            cmd2 = 'git diff ' + x + ' ' + x2

            os.system(cmd2)

        else:
            print("No valid option!")
