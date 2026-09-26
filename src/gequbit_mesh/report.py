import numpy as np
from .core import percent_change

def convergence_summary(mesh_labels, values, tolerance_percent=1.0):
    vals=np.asarray(values,float)
    if len(mesh_labels)!=len(vals) or len(vals)<2:
        raise ValueError("need matching labels and at least two values")
    rows=[]
    for i in range(1,len(vals)):
        shift=float(percent_change(vals[i-1],vals[i]))
        rows.append({"from":mesh_labels[i-1],"to":mesh_labels[i],"value":float(vals[i]),"percent_shift":shift})
    passed=abs(rows[-1]["percent_shift"])<=tolerance_percent
    return {"rows":rows,"latest_passes_tolerance":passed,"tolerance_percent":float(tolerance_percent)}

def max_component_percent_change(a, b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    if a.shape!=b.shape:
        raise ValueError("shape mismatch")
    denom=np.maximum(np.abs(a),np.finfo(float).tiny)
    return float(np.max(np.abs((b-a)/denom))*100)
