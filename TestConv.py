import unittest
import pydot
from conv import Conv

class TestConv(unittest.TestCase):

    def __init__(self) :
        self.converter = Conv()

    def test_get_files_size(self):
        self.converter.getFiles()
        self.assertNotEqual(len(self.converter.files), 0)

    def test_get_words_size(self):
        self.converter.getWords()
        self.assertNotEqual(self.lineCounter, 0)

    def test_save_to_dict_size(self):
        self.converter.saveToDictionary('graph2.py')
        self.assertNotEqual(len(self.converter.fhmap), 0)
        self.assertNotEqual(len(self.converter.all_func_dict), 0)

if __name__ == '__main__':
    unittest.main()
