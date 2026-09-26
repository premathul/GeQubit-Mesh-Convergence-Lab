import numpy as np

def absolute_change(coarse, fine):
    return np.asarray(fine,float)-np.asarray(coarse,float)

def relative_change(coarse, fine):
    c=np.asarray(coarse,float); f=np.asarray(fine,float)
    denom=np.maximum(np.abs(c),np.finfo(float).tiny)
    return (f-c)/denom

def percent_change(coarse, fine):
    return 100.0*relative_change(coarse,fine)

def observed_order_equal_ratio(q_coarse, q_mid, q_fine, refinement_ratio):
    if refinement_ratio <= 1:
        raise ValueError("refinement_ratio must exceed 1")
    a=np.asarray(q_coarse,float); b=np.asarray(q_mid,float); c=np.asarray(q_fine,float)
    num=np.abs(a-b); den=np.abs(b-c)
    if np.any(den==0) or np.any(num==0):
        raise ValueError("nonzero successive differences required")
    return np.log(num/den)/np.log(refinement_ratio)

def richardson_extrapolate(q_mid, q_fine, refinement_ratio, order):
    if refinement_ratio <= 1:
        raise ValueError("refinement_ratio must exceed 1")
    r=refinement_ratio
    return np.asarray(q_fine,float)+(np.asarray(q_fine,float)-np.asarray(q_mid,float))/(r**order-1)
