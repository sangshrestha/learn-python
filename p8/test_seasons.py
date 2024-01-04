from seasons import say_num
import random


def main():
    for _ in range(100):
        n = f"{random.randint(0,9)}"
        for _ in range(7):
            n += f"{random.randint(0,2)}"
        print(f"{int(n):,}", say_num(int(n)))


def test_zero():
    assert say_num(0) == "Zero"


if __name__ == "__main__":
    main()
