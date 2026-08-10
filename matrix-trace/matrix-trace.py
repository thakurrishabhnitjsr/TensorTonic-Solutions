import numpy as np

def matrix_trace(A):
    shape=np.shape(A)
    N=shape[0]
    sum=0
    for i in range(N):
        sum+=A[i][i]
    return sum
    pass
