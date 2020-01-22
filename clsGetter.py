import os
import json

class ClsGetter:

    def __init__(self) :
        self.cls = "class"
        self.cls_names = []
        self.cls_dict = {}
        self.all_cls_dict = {}
        self.lineCounter = 0

    def getCls(self, lines) :
        n=1
        self.lineCounter = 0
        for line in lines:

            if self.cls in line:
                list_of_cls_names = line.split()
                word = list_of_cls_names[1]
                if word is not "=":
                    self.cls_names.append(word)

        #dodane
    def saveClsToDict(self,fil, lines) :
        cls_counter=0
        for name in self.cls_names:
            for line in lines:
                if str(name) in line:
                    if (name!='1'and name!='2' and name!='1,'):
                        cls_counter = cls_counter + 1
                        self.cls_dict[name] = cls_counter
            cls_counter = 0


        self.all_cls_dict['data.json'] =  {}
        self.all_cls_dict['func.json'] =  {}
        self.all_cls_dict['relfunc.json'] =  {}
        self.all_cls_dict['cls.json'] =  {}
        self.all_cls_dict[str(fil)] = self.cls_dict
        self.cls_dict = {}





    def saveClsDictToJson(self) :

        with open('cls.json', 'w') as js_file:
            data = json.dump(self.all_cls_dict, js_file, indent=2)
