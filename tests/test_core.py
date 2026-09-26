import numpy as np
from gequbit_mesh.core import observed_order_equal_ratio, richardson_extrapolate
from gequbit_mesh.report import convergence_summary

def test_second_order_sequence():
    q0=2.0
    vals=[q0+1.0, q0+0.25, q0+0.0625]
    p=observed_order_equal_ratio(*vals, refinement_ratio=2.0)
    assert np.isclose(p,2.0)
    ext=richardson_extrapolate(vals[1],vals[2],2.0,p)
    assert np.isclose(ext,q0)

def test_summary_passes():
    s=convergence_summary(["c","b","f"],[10,10.2,10.21],1.0)
    assert s["latest_passes_tolerance"]
