from gequbit_mesh.report import convergence_summary

meshes=["coarse","baseline","fine"]
values=[7.05,7.18,7.19]
print(convergence_summary(meshes,values,tolerance_percent=1.0))
