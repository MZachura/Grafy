import os
import json


df = "def"
imp = "import"
path = "/Users/marcinzachura/PycharmProjects/untitled/grafy/Grafy"
files = []
words = []
fhmap = {}
hmap = {}
counter = 0
lines = ()
lineCounter = 0

func_names = []
func_counter = 0
func_dict = {}
all_func_dict = {}

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
    print(func_names)


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
        if df in line:
            list_of_func_names = line.split();
            word = list_of_func_names[1]
            if word is not "=":
                func_names.append(word)
    lineCounter = 0

def saveToDictionary(fil):
    global counter
    global hmap
    global func_dict
    global func_counter
    for w in words:
        for line in lines:
            if str(w) in line:
                counter = counter + 1
                hmap[w] = counter
        counter = 0
    for name in func_names:
        for line in lines:
            if str(name) in line:
                func_counter = func_counter + 1
                func_dict[name] = func_counter
        func_counter = 0
    fhmap[str(fil)] = hmap
    all_func_dict[str(fil)] = func_dict;
    hmap = {}
    func_dict = {}


def saveToFile():
    with open('data.json', 'w') as js_file:
        data = json.dump(fhmap, js_file)
    with open('func.json', 'w') as js_file:
        data = json.dump(all_func_dict, js_file,indent=2,)

main()
