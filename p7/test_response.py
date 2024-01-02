from response import check_email


def test_valid():
    assert check_email("malan@harvard.edu") == True


def test_invalid():
    assert check_email("malan@@@harvard.edu") == False
