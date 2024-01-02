from working import convert
import pytest


def test_am_to_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_colon():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_pm_to_am():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_to_error():
    with pytest.raises(ValueError):
        convert("9:59 AM - 5:59 PM")
