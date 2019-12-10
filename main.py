from graph2 import Graph2
from conv import Conv
from control import Control

def main() :
    # global lines
    # global words
    converter = Conv()
    graph = Graph2()
    control = Control()

    converter.getFiles()
    for fil in converter.files:
        if 'pyparsing.py' not in str(fil):
            converter.lines = tuple(open(str(fil), 'r', encoding='latin-1'))
            converter.getWords()
            converter.saveToDictionary(fil)
            converter.words = []
    converter.saveToFile()
    #graph.drawAllGraph()
    control.askForGraphType()
    control.drawCombinationOfGraph()

    # graph.drawGraph()
    # graph.drawGrafFunkcji()
    # graph.drawGrafModulu()

main()
