
class PythonTemplate:
    def __init__(self, args=None):
        self._args = args if args is not None else []


    def class_defn(self, class_name):
        text = f'''class {class_name}:

    def __init__(self, args=None):
        self._args = args if args is not None else []
'''
        return text

if __name__ == '__main__':
    t = PythonTemplate()
    print(t.class_defn('PythonTemplate'))
