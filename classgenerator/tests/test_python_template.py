from classgenerator.scripts.python_template import PythonTemplate


def test_make_empty_python_template():
    t = PythonTemplate()
    assert t is not None


def test_python_template_class_defn():
    t = PythonTemplate()
    class_t = t.class_defn("PythonTemplate")
    assert class_t is not None
