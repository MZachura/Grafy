import os

class FileGetter:

    def __init__(self) :
        self.files = []
        self.path = "/Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy"


    def getFiles(self) :
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.py' in file:
                    if '.pyc' not in file:
                        self.files.append(file)
                if '.json' in file:
                    self.files.append(file)
