from fuel import gauge, convert
import pytest


def test_division():
    assert convert("3/4") == 75


def test_value_err():
    with pytest.raises(ValueError):
        convert("5/4")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge_full():
    assert gauge(99) == "F"


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_num():
    assert gauge(25) == "25%"
