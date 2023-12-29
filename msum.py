import numpy as np


def main():
    A = np.array([1, 2, 3, 1, 4, 1, 2, 1, 9]).reshape(-1, 3)
    C = np.array([2, -1, 0, -1, 1, 0, -2, 1, 1]).reshape(-1, 3)
    a, b = 4, -7
    print(np.dot(C, A), sep="\n\n")


if __name__ == "__main__":
    main()
