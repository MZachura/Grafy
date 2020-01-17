import os
import json

class ClsGetter:

    def __init__(self) :
        self.cls = "class"
        # self.path = "/Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy"
        # self.files = []
        # self.words = []
        # self.fhmap = {} - k
        # self.hmap = {} - k
        # self.lines = ()
        # self.func_names = []
        self.cls_names = []
        # self.rel_func_names = []    #dodane
        # self.func_dict = {}
        # self.rel_dict = {}
        self.cls_dict = {}
        # self.all_func_dict = {}
        # self.all_func_rel_dict = {}
        self.all_cls_dict = {}
        self.lineCounter = 0

    # def getFiles(self) :
    #     # r=root, d=directories, f = files
    #     for r, d, f in os.walk(self.path):
    #         for file in f:
    #             if '.py' in file:
    #                 if '.pyc' not in file:
    #                     self.files.append(file)
    #             if '.json' in file:
    #                 self.files.append(file)

    def getCls(self, lines) :
        n=1
        self.lineCounter = 0
        for line in lines:
            # if '\n' in line:
                # self.lineCounter = self.lineCounter + 1
                # self.hmap['lines'] = self.lineCounter

            # if self.imp in line:
            #     list_of_words = line.split()
            #     word = list_of_words[1]
            #     if word is not "=":
            #         self.words.append(word)
            #
            # if self.exp in line:
            #     list_of_words = line.split()
            #     word = list_of_words[1]
            #     word= word[6:-2]
            #     if word is not "=":
            #         if word is not "":
            #             self.words.append(word)

            # if self.df in line:
            #     list_of_func_names = line.split()
            #     word = list_of_func_names[1]
            #     if word is not "=":
            #         self.func_names.append(word)

            if self.cls in line:
                list_of_cls_names = line.split()
                word = list_of_cls_names[1]
                # print(list_of_cls_names)
                if word is not "=":
                    self.cls_names.append(word)

        #dodane
    def saveClsToDict(self,fil, lines) :
        # func_counter = 0
        # counter = 0
        cls_counter=0
        # rel_counter=0
        # for w in self.words:
        #     for line in self.lines:
        #         if str(w) in line:
        #             counter = counter + 1
        #             self.hmap[w] = counter
        #     counter = 0
        # for name in self.func_names:
        #     if (name!='1'and name!='2' and name!='1,'):
        #         for line in lines:
        #             if str(name) in line:
        #                 func_counter = func_counter + 1
        #                 self.func_dict[name] = func_counter
        #     func_counter = 0
        for name in self.cls_names:
            for line in lines:
                if str(name) in line:
                    if (name!='1'and name!='2' and name!='1,'):
                        cls_counter = cls_counter + 1
                        self.cls_dict[name] = cls_counter
            cls_counter = 0

        #dodane
        # for name in self.rel_func_names:
        #     for line in lines:
        #         if name in line:
        #             rel_counter = rel_counter + 1
        #             self.rel_dict[name] = rel_counter
        #     rel_counter = 0

        # self.fhmap[str(fil)] = self.hmap
        # self.all_func_dict['func.json'] =  {}
        # self.all_func_dict['data.json'] =  {}
        # self.all_func_dict[str(fil)] = self.func_dict
        # self.all_func_rel_dict['func.json'] =  {}
        # self.all_func_rel_dict['relfunc.json'] =  {}
        # self.all_func_rel_dict[str(fil)] = self.rel_dict #dodane
        self.all_cls_dict['data.json'] =  {}
        self.all_cls_dict['func.json'] =  {}
        self.all_cls_dict['relfunc.json'] =  {}
        self.all_cls_dict['cls.json'] =  {}
        self.all_cls_dict[str(fil)] = self.cls_dict
        # self.hmap = {}
        # self.func_dict = {}
        self.cls_dict = {}
        # self.rel_dict = {} #dodane



    # def relFunc(self,lines) :
    #     for line in lines:
    #         if '\n' in line:
    #             self.lineCounter = self.lineCounter + 1
    #             self.hmap['lines'] = self.lineCounter
    #
    #         for name in self.all_func_dict:
    #             for data in self.all_func_dict[name]:
    #                 if(data=="saveToDictionary(self,fil)"):
    #                     data=data[:-10]
    #                 else:
    #                     data=data[:-6]
    #                 if data in line:
    #                     if(self.df not in line):
    #                         list_of_related_func=line.split()
    #                         if("#" not in line):
    #                             word = data
    #                             self.rel_func_names.append(word)
    #                     list_of_related_func=line.split()
    #                     if(list_of_related_func!=0):
    #                         if("#" not in line):
    #                             word = data
    #                             self.rel_func_names.append(word)


    def saveClsDictToJson(self) :
        # with open('data.json', 'w') as js_file:
        #     data = json.dump(self.fhmap, js_file,indent=2)
        # with open('func.json', 'w') as js_file:
        #     data = json.dump(self.all_func_dict, js_file, indent=2)
        with open('cls.json', 'w') as js_file:
            data = json.dump(self.all_cls_dict, js_file, indent=2)
        # with open('relfunc.json', 'w') as js_file:
        #     data = json.dump(self.all_func_rel_dict, js_file, indent=2)