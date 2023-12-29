from bank import value


def test_hello():
    assert value("hello") == 0


def test_starts_with_h():
    assert value("hey") == 20


def test_100():
    assert value("feliz navidad") == 100
