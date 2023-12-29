from twttr import shorten


def test_no_vowel():
    assert shorten("rhythm") == "rhythm"


def test_vowels():
    assert shorten("aeiou") == ""


def test_upper():
    assert shorten("HELLO") == "HLL"
