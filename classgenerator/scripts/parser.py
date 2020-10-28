from sys import argv
import json
import os
from python_template import PythonTemplate
from puml_template import PUMLTemplate
from name_case import NameCase 

class Parser:
    def __init__(self, args=None):
        self._args = args if args is not None else []

    def check_args(self):
        self._injson = self._args[1]

    def parse(self):
        infile = open(self._injson,'r')
        data = json.load(infile)
        # Create output directory
        output_dirname = 'parser_output'  
        try:
            os.makedirs(output_dirname)
        except OSError:
            exit("Error: output directory exists")

        t = PythonTemplate()
        p = PUMLTemplate()
        puml_file = open(output_dirname + '/class.puml', 'w')
        puml_file.write(p.header())
        for cl in data: 
            classname = cl['class']
            filename = output_dirname + '/' + NameCase.to_py_name(classname)
            
            with open(filename, 'w') as outfile:
                outfile.write(t.class_defn(classname))

            puml_file.write(p.class_defn(classname))
        puml_file.write(p.footer())


if __name__ == '__main__':
    p = Parser(argv)
    #breakpoint()
    p.check_args()
    p.parse()
    