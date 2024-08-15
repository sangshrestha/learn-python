import numpy as np


def main():
    A = np.array([0.5, -0.25, -0.25, 0.9]).reshape(-1, 2)
    C = np.array([7 / 4, 1, -1 / 2]).reshape(-1, 1)
    print(np.dot(np.linalg.inv(A), [7000, 14000]), sep="\n\n")


if __name__ == "__main__":
    main()
