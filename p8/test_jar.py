from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_store():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2


def test_take():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(1)
    assert jar.size == 10


def test_greedy():
    jar = Jar()

    with pytest.raises(ValueError):
        jar.withdraw(100)
