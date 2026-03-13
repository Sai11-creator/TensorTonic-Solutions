import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    vect = np.array(X,dtype = float)
    mean = np.mean(vect,axis = axis,keepdims = True)
    std = np.std(vect,axis = axis, keepdims=True)
    
    return (vect-mean)/(std+eps)
