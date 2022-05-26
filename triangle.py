# by : Abdolah Khoshkalam






# This is Khayyam Pascal triangle programm with Python and Numpy
import numpy as np
def tri(n): # This function print triangle of numbers.
    mat = np.zeros((n, n)) # Difine a zero array inside an empty array
    for i in range(n): # Number of rows
        for j in range(n): # Number of columns
            mat[0, 0] = mat[1, 0] = mat[1, 1] = 1 # Value of three first datas
            mat[i, j] = mat[i-1, j] + mat[i-1, j-1] # Value of another left-down data
            mat[i, i] = 1 # Value of datas in main diameter is one
            mat[i, 0] = 1 # Value of first column is one
            if (i<j): # actually we have a triangular top matrix
                mat[i, j] = 0
    # Show output part
    for i in range(n): # number of rows
        for j in range(n): # Number of columns
            if mat[i, j] != 0: # We only need non-zero datas
                print((mat[i, j]), end = "  ")
        print()

n = int(input("number of rows : ")) # Get number of rows
tri(n) # Function calling