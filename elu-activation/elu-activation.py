def elu(x, alpha):
    import numpy as np
    klist=[]
    for i in x:
        if i>0:
            klist.append(float(i))
        else:
            x=alpha*(np.exp(i)-1)
            klist.append(float(x))
    return klist
    # Write code here