from classgenerator.scripts.parser import Parser


def test_make_empty_parser():
    p = Parser()
    assert p is not None
    assert isinstance(p, Parser)
