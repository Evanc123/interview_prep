import numpy as np

def binomial_coefficient(n, k):
    size = 1000
    bc = np.zeros((size, size))
    for i in range(size):
        bc[i][i] = 1
        bc[i][0] = 1
    for i in range(1, size):
        for j in range(1, i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
    return bc[n][k]


print binomial_coefficient(500, 499)