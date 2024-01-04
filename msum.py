import numpy as np


def main():
    A = np.array([1, 0, 0, -2, 3, 0, 2, 4, 1]).reshape(-1, 3)
    B = np.array([2, -1, 3, 0, 1, 2, 0, 0, 4]).reshape(-1, 3)
    C = np.array([7 / 4, 1, -1 / 2]).reshape(-1, 1)
    a, b = 4, -7
    print(np.dot(np.dot(A, B), C), sep="\n\n")


if __name__ == "__main__":
    main()
