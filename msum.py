import numpy as np


def main():
    A = np.array([2, 1, 2, 2, 2, -2, 3, 1, 1]).reshape(-1, 3)
    C = np.array([0, 6, 0]).reshape(-1, 1)
    a, b = 4, -7
    print(np.dot(A, C), sep="\n\n")


if __name__ == "__main__":
    main()
