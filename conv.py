import os
import json

imp = "import"
path = "/Users/marcinzachura/PycharmProjects/untitled/NOWY"
files = []
words = []
fhmap = {}
hmap = {}
counter = 0
lines = ()
lineCounter = 0

def main():
    global lines
    global words
    getFiles()
    for fil in files:
        if 'pyparsing.py' not in str(fil):
            lines = tuple(open(str(fil), 'r', encoding='latin-1'))
            getWords()
            saveToDictionary(fil)
            words = []
    saveToFile()

def getFiles():
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.py' in file:
                if '.pyc' not in file:
                    files.append(file)

def getWords():
    global lines
    global lineCounter
    for line in lines:
        if '\n' in line:
            lineCounter = lineCounter + 1
            hmap['lines'] = lineCounter
        if imp in line:
            list_of_words = line.split()
            word = list_of_words[1]
            if word is not "=":
                words.append(word)
    lineCounter = 0

def saveToDictionary(fil):
    global counter
    global hmap
    for w in words:
        for line in lines:
            if str(w) in line:
                counter = counter + 1
                hmap[w] = counter
        counter = 0
    fhmap[str(fil)] = hmap
    hmap = {}


def saveToFile():
    with open('data.json', 'w') as js_file:
        data = json.dump(fhmap, js_file)


main()
print(lineCounter)
