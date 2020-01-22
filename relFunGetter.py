import os
import json

class RelFuncGetter:

    def __init__(self)  :
        self.rel_func_names = []    #dodane
        self.func_dict = {}
        self.rel_dict = {}
        self.all_func_dict= {}
        self.lineCounter = 0
    def saveClsToDict(self,fil, lines) :
        rel_counter=0

        for name in self.rel_func_names:
             for line in lines:
                 if name in line:
                     rel_counter = rel_counter + 1
                     self.rel_dict[name] = rel_counter
             rel_counter = 0

    def relFunc(self,lines) :
        for line in lines:
            if '\n' in line:
                self.lineCounter = self.lineCounter + 1
                self.hmap['lines'] = self.lineCounter

            for name in self.all_func_dict:
                for data in self.all_func_dict[name]:
                    if(data=="saveToDictionary(self,fil)"):
                        data=data[:-10]
                    else:
                        data=data[:-6]
                    if data in line:
                        if(self.df not in line):
                            list_of_related_func=line.split()
                            if("#" not in line):
                                word = data
                                self.rel_func_names.append(word)
                        list_of_related_func=line.split()
                        if(list_of_related_func!=0):
                            if("#" not in line):
                                word = data
                                self.rel_func_names.append(word)
