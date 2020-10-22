from sys import argv
import json

class Parser:
    def __init__(self, args=None):
        self._args = args if args is not None else []

    def check_args(self):
        print(len(self._args))
        self._injson = self._args[1]

    def parse(self):
        infile = open(self._injson,'r')
        data = json.load(infile)
        for cl in data:
            print(cl['class'])


if __name__ == '__main__':
    p = Parser(argv)
    breakpoint()
    p.check_args()
    p.parse()
    