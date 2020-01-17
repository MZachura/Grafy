import os
import json

class FuncGetter:

    def __init__(self) :
        self.func_names = []
        self.func_dict = {}
        self.lineCounter = 0
        self.all_func_dict= {}
        self.df = "def"

    def getFunc(self, lines) :
        self.lineCounter = 0
        for line in lines:
            if self.df in line:
                list_of_func_names = line.split()
                word = list_of_func_names[1]
                if word is not "=":
                    self.func_names.append(word)

    def saveFuncsToDict(self, fil, lines) :
        func_counter = 0
        for name in self.func_names:
            if (name!='1'and name!='2' and name!='1,'):
                for line in lines:
                    if str(name) in line:
                        func_counter = func_counter + 1
                        self.func_dict[name] = func_counter
            func_counter = 0
            self.all_func_dict[str(fil)] = self.func_dict
        self.func_dict = {}

    def saveFuncDictToJson(self) :
        self.all_func_dict['relfunc.json'] =  {}
        self.all_func_dict['cls.json'] =  {}
        self.all_func_dict['func.json'] =  {}
        self.all_func_dict['data.json'] =  {}
        with open('func.json', 'w') as js_file:
            data = json.dump(self.all_func_dict, js_file, indent=2)
#
