import numpy as np

def make_diagonal(v):
    N=len(v)
    ans=[]
    for i in range(N):
        new_row=[]
        for j in range(N):
            if i==j:
                new_row.append(v[i])
            else: new_row.append(0)
        ans.append(new_row)
    return np.array(ans)
    pass
