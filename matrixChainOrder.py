# ---------------------------------------------------------------------
# Author: Subhashis Suara
# Algorithm: Matrix Chain Ordering
# Definations:
#   P - Matrix Order Array
#   C - Minimum No. of Scalar Multiplications per Matrix Chain
#   S - Value of k (Separating Point) for which C element was obtained
# ---------------------------------------------------------------------

import sys

def matrixChainOrder(P):
    n = len(P) - 1 # Number of Matrices
    C = [[None for i in range(n)] for j in range(n)]
    S = [[None for i in range(n)] for j in range(n)]
    
    for i in range(n):
        C[i][i] = 0
        S[i][i] = 0
    
    for l in range(2, n + 1): # Number of Matrices in each Chain
        for i in range(1, (n - l + 1) + 1): # First Matrix of Chain
            j = i + l - 1 # Last Matrix of Chain
            # Below is Adjusted for 0 based Indexing
            C[i - 1][j - 1] = sys.maxsize
            for k in range(i, j):
                x = C[i - 1][k - 1] + C[(k + 1) - 1][j - 1] + P[i - 1] * P[k] * P[j]
                if (C[i - 1][j - 1] > x):
                    C[i - 1][j - 1] = x
                    S[i - 1][j - 1] = k

    return C, S

def printMatrixChain(S, i, j):
    if (i == j):
        print(f"A{i}", end = "")
    else:
        print("(", end = "")
        # Below is Adjusted for 0 based Indexing
        printMatrixChain(S, i, S[i - 1][j - 1])
        printMatrixChain(S, S[i - 1][j - 1] + 1, j)
        print(")", end = "")

if __name__ == "__main__":
    # P = [4, 10, 3, 12, 20, 7]
    size = int(input("\nEnter the number of elements in Matrix Order Array: "))
    P = []
    print("\nEnter the elements:")
    for i in range(size):
        P.append(int(input()))
    n = len(P) - 1 # Number of Matrices
    C, S =  matrixChainOrder(P)
    print("\nMatrix chain for minimum no. of scalar multiplication:")
    printMatrixChain(S, 1, n)
    print("\n")