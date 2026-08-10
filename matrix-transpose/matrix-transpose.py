import numpy as np

def matrix_transpose(A):
    ax=np.array(A)
    shape=ax.shape
    row=shape[0]
    column=shape[1]
    b=[]
    for i in range(column):
        new_row=[]
        for j in range(row):
            new_row.append(A[j][i])
        b.append(new_row)
    return np.array(b)
    
    pass
