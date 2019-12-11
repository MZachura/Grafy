import os
import json

class Conv:

    def __init__(self) :
        self.df = "def"
        self.cls = "class"
        self.imp = "import"
        self.path = "/Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy"
        self.files = []
        self.words = []
        self.fhmap = {}
        self.hmap = {}
        self.lines = ()
        self.func_names = []
        self.cls_names = []
        self.func_dict = {}
        self.cls_dict = {}
        self.all_func_dict = {}
        self.all_cls_dict = {}
        self.lineCounter = 0

    def getFiles(self) :
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.py' in file:
                    if '.pyc' not in file:
                        self.files.append(file)

    def getWords(self) :
        n=1
        self.lineCounter = 0
        for line in self.lines:
            if '\n' in line:
                self.lineCounter = self.lineCounter + 1
                self.hmap['lines'] = self.lineCounter
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


            if self.cls in line:
                list_of_cls_names = line.split();
                word = list_of_cls_names[1]
                if word is not "=":
                    self.cls_names.append(word)
        # lineCounter = 0 to moze byz zjebane

    def saveToDictionary(self,fil) :
        func_counter = 0
        counter = 0
        cls_counter=0
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
        for name in self.cls_names:
            for line in self.lines:
                if str(name) in line:
                    cls_counter = cls_counter + 1
                    self.cls_dict[name] = cls_counter
            cls_counter = 0
        self.fhmap[str(fil)] = self.hmap
        self.all_func_dict[str(fil)] = self.func_dict;
        self.all_cls_dict[str(fil)] = self.cls_dict;
        self.hmap = {}
        self.func_dict = {}
        self.cls_dict = {}


    def saveToFile(self) :
        with open('data.json', 'w') as js_file:
            data = json.dump(self.fhmap, js_file,indent=2)
        with open('func.json', 'w') as js_file:
            data = json.dump(self.all_func_dict, js_file, indent=2)
        with open('cls.json', 'w') as js_file:
            data = json.dump(self.all_cls_dict, js_file, indent=2)
