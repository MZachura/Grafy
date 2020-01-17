import unittest
import pydot
from clsGetter import ClsGetter
from fileGetter import FileGetter
from funcGetter import FuncGetter
from wordGetter import WordGetter

class TestGetters(unittest.TestCase) :

    # def __init__(self) :
    #     self.converter = Conv()
    #     self.control = Control()

    # def test_get_files_size(self) :
    #     self.clsGetter = ClsGetter()
    #     # self.control = Control()
    #     self.clsGetter.getCls()
    #     self.assertNotEqual(len(self.clsGetter.files), 0)

    def test_file_getter_get_files_size(self) :
        fileGetter = FileGetter()
        fileGetter.getFiles()
        self.assertNotEqual(len(fileGetter.files), 0)

    def test_cls_getter_get_cls_size(self) :
        clsGetter = ClsGetter()
        fileGetter = FileGetter()
        fileGetter.getFiles()
        for fil in fileGetter.files:
            if 'pyparsing.py' not in str(fil):
                lines = tuple(open(str(fil), 'r', encoding='latin-1'))
                clsGetter.getCls(lines)
        self.assertNotEqual(len(clsGetter.cls_names), 0)

    def test_func_getter_get_func_size(self) :
        funcGetter = FuncGetter()
        fileGetter = FileGetter()
        fileGetter.getFiles()
        for fil in fileGetter.files:
            if 'pyparsing.py' not in str(fil):
                lines = tuple(open(str(fil), 'r', encoding='latin-1'))
                funcGetter.getFunc(lines)
        self.assertNotEqual(len(funcGetter.func_names), 0)

    def test_word_getter_get_word_size(self) :
        wordGetter = WordGetter()
        fileGetter = FileGetter()
        fileGetter.getFiles()
        for fil in fileGetter.files:
            if 'pyparsing.py' not in str(fil):
                lines = tuple(open(str(fil), 'r', encoding='latin-1'))
                wordGetter.getWords(lines)
        self.assertNotEqual(len(wordGetter.words), 0)




        # def test_get_words_size(self) :
    #     self.converter = Conv()
    #     self.converter.getFiles()
    #     for fil in self.converter.files:
    #         if 'pyparsing.py' not in str(fil):
    #             self.converter.lines = tuple(open(str(fil), 'r', encoding='latin-1'))
    #             self.converter.getWords()
    #     self.assertNotEqual(len(self.converter.func_names), 0)
    #
    # def test_save_to_dict_size(self) :
    #     self.converter = Conv()
    #     self.converter.saveToDictionary('graph2.py')
    #     self.assertNotEqual(len(self.converter.fhmap), 0)
    #     self.assertNotEqual(len(self.converter.all_func_dict), 0)
    #     self.assertNotEqual(len(self.converter.all_cls_dict), 0)
    #     self.assertNotEqual(len(self.converter.all_func_rel_dict), 0)

if __name__ == '__main__':
    unittest.main()
