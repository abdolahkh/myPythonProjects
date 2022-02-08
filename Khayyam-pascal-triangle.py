import numpy as np
def tri(n):
    mat = np.ones((n, n))
    for i in range(n):
        for j in range(n):
            mat[0, 0] = mat[1, 0] = mat[1, 1] = 1
            mat[i, j] = mat[i-1, j] + mat[i-1, j-1]
            mat[i, i] = 1
            mat[i, 0] = 1
            if (i<j):
                mat[i, j] = 0
    # c = n
    for i in range(n):
        # print(c*' ', end = '')
        for j in range(n):
            if mat[i, j] != 0:
                print((mat[i, j]), end = "  ")
        print()
        # c -= 1

n = int(input("number of rows : "))
tri(n)