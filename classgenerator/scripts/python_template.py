
class PythonTemplate:
    def __init__(self, args=None):
        self._args = args if args is not None else []


    def class_defn(self, class_name):
        text = f'''class {class_name}:\ndef __init__(self, args=None):\n    self._args = args if args is not None else []\n'''
        return text

