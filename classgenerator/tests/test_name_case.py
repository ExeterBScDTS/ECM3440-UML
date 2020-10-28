from classgenerator.scripts.name_case import NameCase


def test_make_empty_name_case():
    n = NameCase()
    assert n is not None
    assert isinstance(n, NameCase)

def test_short_name():
    fname = NameCase.to_py_name("Parser")
    assert fname == "parser.py"

def test_long_name():
    fname = NameCase.to_py_name("NameCase")
    assert fname == "name_case.py"

def test_complicated_name():
    fname = NameCase.to_py_name("HTTPIsAProtocol")
    assert fname == "http_is_a_protocol.py"
