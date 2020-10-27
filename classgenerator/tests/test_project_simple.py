from classgenerator.scripts.parser import Parser


def test_simple_project():
    p = Parser(['test','classgenerator/samples/simple.json'])
    p.check_args()
    p.parse()

