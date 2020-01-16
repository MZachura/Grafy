import os
import json

class WordGetter:

    def __init__(self) :
        self.imp = "import"
        self.exp = "open('"
        self.fhmap = {}
        self.hmap = {}
        self.words = []
        self.lineCounter = 0


    def getWords(self, lines) :
        self.lineCounter = 0
        for line in lines:
            if '\n' in line:
                self.lineCounter = self.lineCounter + 1
                self.hmap['lines'] = self.lineCounter

            if self.imp in line:
                list_of_words = line.split()
                word = list_of_words[1]
                if list_of_words is not "=":
                    if word is not "=":
                        if list_of_words is not "imp":
                            self.words.append(word)

            if self.exp in line:
                list_of_words = line.split()
                word = list_of_words[1]
                word= word[6:-2]
                if word is not "=":
                    if word is not "":
                        self.words.append(word)

    def saveWordsToDict(self, fil, lines) :
        counter = 0
        for w in self.words:
            for line in lines:
                if str(w) in line:
                    counter = counter + 1
                    self.hmap[w] = counter
            counter = 0
        self.fhmap[str(fil)] = self.hmap
        self.hmap = {}

    def saveDictToJson(self) :
        with open('data.json', 'w') as js_file:
            data = json.dump(self.fhmap, js_file,indent=2)
