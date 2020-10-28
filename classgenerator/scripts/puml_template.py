
class PUMLTemplate:
    def __init__(self, args=None):
        self._args = args if args is not None else []


    def class_defn(self, class_name):
        text = (f'class {class_name} ' '{\n' '}\n\n')
        return text

    def header(self):
        return '@startuml\n'

    def footer(self):
        return '@enduml\n'

