import re

class NameCase:
    @staticmethod
    def to_py_name(classname):
        filename = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', classname)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', filename).lower()+'.py'
