from graph2 import Graph2
from conv import Conv
from control import Control
from fileGetter import FileGetter
from wordGetter import WordGetter

def main() :

    converter = Conv()
    graph = Graph2()
    control = Control()
    fileGetter = FileGetter()
    wordGetter = WordGetter()

    fileGetter.getFiles()
    for fil in fileGetter.files:
        if 'pyparsing.py' not in str(fil):
            lines = tuple(open(str(fil), 'r', encoding='latin-1'))
            converter.getWords(lines)
            wordGetter.getWords(lines)
            converter.saveToDictionary(fil, lines)
            wordGetter.saveWordsToDict(fil, lines)
            wordGetter.words = []
    converter.saveToFile()
    wordGetter.saveDictToJson()
    # converter.relFunc()
    control.askForGraphType()
    control.drawCombinationOfGraph()

main()
