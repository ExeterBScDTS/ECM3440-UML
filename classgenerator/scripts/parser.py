from sys import argv
import json
from python_template import PythonTemplate

class Parser:
    def __init__(self, args=None):
        self._args = args if args is not None else []

    def check_args(self):
        self._injson = self._args[1]

    def parse(self):
        infile = open(self._injson,'r')
        data = json.load(infile)
        t = PythonTemplate()
        for cl in data:
            #print(cl['class'])  
            classname = cl['class']
            print(t.class_defn(classname))
            print()


if __name__ == '__main__':
    p = Parser(argv)
    #breakpoint()
    p.check_args()
    p.parse()
    