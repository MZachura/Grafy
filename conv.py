import os
import json
from graph2 import Graph2

class Conv:

    def __init__(self) :
        self.df = "def"
        self.imp = "import"
        self.path = "/Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy"
        self.files = []
        self.words = []
        self.fhmap = {}
        self.hmap = {}
        self.lines = ()
        self.func_names = []
        self.func_dict = {}
        self.all_func_dict = {}


    def getFiles(self) :
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.py' in file:
                    if '.pyc' not in file:
                        self.files.append(file)

    def getWords(self) :
        lineCounter = 0
        for line in self.lines:
            if '\n' in line:
                lineCounter = lineCounter + 1
                self.hmap['lines'] = lineCounter
            if self.imp in line:
                list_of_words = line.split()
                word = list_of_words[1]
                if word is not "=":
                    self.words.append(word)
            if self.df in line:
                list_of_func_names = line.split();
                word = list_of_func_names[1]
                if word is not "=":
                    self.func_names.append(word)
        lineCounter = 0

    def saveToDictionary(self,fil) :
        func_counter = 0
        counter = 0
        for w in self.words:
            for line in self.lines:
                if str(w) in line:
                    counter = counter + 1
                    self.hmap[w] = counter
            counter = 0
        for name in self.func_names:
            for line in self.lines:
                if str(name) in line:
                    func_counter = func_counter + 1
                    self.func_dict[name] = func_counter
            func_counter = 0
        self.fhmap[str(fil)] = self.hmap
        self.all_func_dict[str(fil)] = self.func_dict;
        self.hmap = {}
        self.func_dict = {}


    def saveToFile(self) :
        with open('data.json', 'w') as js_file:
            data = json.dump(self.fhmap, js_file,indent=2)
        with open('func.json', 'w') as js_file:
            data = json.dump(self.all_func_dict, js_file, indent=2)

    def drawGraph(self) :
        graph2 = Graph2()
        graph2.drawGraph()


def main() :
    # global lines
    # global words
    converter = Conv()
    converter.getFiles()
    for fil in converter.files:
        if 'pyparsing.py' not in str(fil):
            converter.lines = tuple(open(str(fil), 'r', encoding='latin-1'))
            converter.getWords()
            converter.saveToDictionary(fil)
            converter.words = []
    converter.saveToFile()
    converter.drawGraph()


main()
