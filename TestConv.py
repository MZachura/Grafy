import unittest
import pydot
from conv import Conv

class TestConv(unittest.TestCase) :

    # def __init__(self) :
    #     self.converter = Conv()
    #     self.control = Control()

    def test_get_files_size(self) :
        self.converter = Conv()
        # self.control = Control()
        self.converter.getFiles()
        self.assertNotEqual(len(self.converter.files), 0)

    def test_get_words_size(self) :
        self.converter = Conv()
        self.converter.getFiles()
        for fil in self.converter.files:
            if 'pyparsing.py' not in str(fil):
                self.converter.lines = tuple(open(str(fil), 'r', encoding='latin-1'))
                self.converter.getWords()
        self.assertNotEqual(len(self.converter.func_names), 0)

    def test_save_to_dict_size(self) :
        self.converter = Conv()
        self.converter.saveToDictionary('graph2.py')
        self.assertNotEqual(len(self.converter.fhmap), 0)
        self.assertNotEqual(len(self.converter.all_func_dict), 0)
        self.assertNotEqual(len(self.converter.all_cls_dict), 0)
        self.assertNotEqual(len(self.converter.all_func_rel_dict), 0)

if __name__ == '__main__':
    unittest.main()
