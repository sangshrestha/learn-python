from um import count


def test_um():
    count("um") == 1


def test_punctuation():
    count("um?") == 1


def test_multiple():
    count("Um, thanks, um...") == 2


def test_part():
    count("Um, thanks for the album.") == 1
