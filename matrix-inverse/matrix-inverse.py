import numpy as np

def matrix_inverse(a):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    ax=np.array(a)
    shape=ax.shape
    ans=[]
    if( shape[0]==shape[1] and ax.ndim==2 ):
        if(np.linalg.det(ax)!=0):
            return np.linalg.inv(ax)
        else: return None
    else: return None
    
    
    pass
