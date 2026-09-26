"""Compare three grid resolutions and estimate discretization order by differences."""
import argparse
import csv
import math

def assess(h, value):
    if len(h) != 3 or len(value) != 3 or not (h[0] > h[1] > h[2] > 0):
        raise ValueError("Provide three coarse-to-fine positive spacings")
    d01, d12 = value[0]-value[1], value[1]-value[2]
    if d01*d12 <= 0:
        return None
    def residual(p):
        return d01/d12 - (h[0]**p-h[1]**p)/(h[1]**p-h[2]**p)
    lo, hi = 0.05, 12.
    if residual(lo)*residual(hi) > 0:
        return None
    for _ in range(100):
        mid = (lo+hi)/2
        if residual(lo)*residual(mid) <= 0: hi=mid
        else: lo=mid
    p=(lo+hi)/2
    continuum=(value[2]*h[1]**p-value[1]*h[2]**p)/(h[1]**p-h[2]**p)
    return p, continuum, abs(continuum-value[2])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv_file", help="Three rows, columns h_nm,value (same physical observable and units)")
    args=p.parse_args()
    with open(args.csv_file,newline="") as f: rows=list(csv.DictReader(f))
    h=[float(r["h_nm"]) for r in rows]
    v=[float(r["value"]) for r in rows]
    result=assess(h,v)
    print("coarse_to_fine_values=",v,"relative_last_shift=",abs(v[-1]-v[-2])/max(abs(v[-1]),1e-300))
    print("observed_order,continuum_estimate,extrapolation_distance=",result)
    if result is None: print("No justified Richardson estimate for these three observations.")
if __name__=="__main__": main()
