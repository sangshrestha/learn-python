import numpy as np

def main():
    A = np.array([4,-3,2,-1]).reshape(-1,2)
    B = np.array([0,1,2,-2,3,1]).reshape(-1,3)
    print(np.dot(A,B))


main()