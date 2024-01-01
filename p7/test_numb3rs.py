from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") == True


def test_limit():
    assert validate("255.255.255.255") == True


def test_all_above():
    assert validate("512.512.512.512") == False


def test_one_above():
    assert validate("1.2.3.1000") == False


def test_string():
    assert validate("cat") == False
