from graph2 import Graph2
from clsGetter import ClsGetter
from control import Control
from fileGetter import FileGetter
from wordGetter import WordGetter
from funcGetter import FuncGetter

def main() :

    clsGetter = ClsGetter()
    graph = Graph2()
    control = Control()
    fileGetter = FileGetter()
    wordGetter = WordGetter()
    funcGetter = FuncGetter()

    fileGetter.getFiles()
    for fil in fileGetter.files:
        if 'pyparsing.py' not in str(fil):
            lines = tuple(open(str(fil), 'r', encoding='latin-1'))
            clsGetter.getCls(lines)
            wordGetter.getWords(lines)
            funcGetter.getFunc(lines)
            clsGetter.saveClsToDict(fil, lines)
            wordGetter.saveWordsToDict(fil, lines)
            funcGetter.saveFuncsToDict(fil, lines)
            wordGetter.words = []
    clsGetter.saveClsDictToJson()
    wordGetter.saveDictToJson()
    funcGetter.saveFuncDictToJson()
    # converter.relFunc(lines)
    control.askForGraphType()
    control.drawCombinationOfGraph()

main()
