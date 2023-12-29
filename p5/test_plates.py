from plates import is_valid


def test_valid():
    assert is_valid("ABC123") == True


def test_min_char():
    assert is_valid("h") == False


def test_max_char():
    assert is_valid("ABCDEFG") == False


def test_starting_num():
    assert is_valid("12ABC") == False


def test_trailing_num():
    assert is_valid("AB12C") == False


def test_special_chars():
    assert is_valid("AB12 ") == False
