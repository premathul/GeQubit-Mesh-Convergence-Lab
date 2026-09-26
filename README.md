# GeQubit-Mesh-Convergence-Lab

GeQubit-Mesh-Convergence-Lab is a research utility for evaluating whether numerical observables from semiconductor quantum-device simulations are stable with respect to mesh refinement. In quantum-dot and spin-qubit modeling, a visually smooth potential or wavefunction does not by itself establish numerical convergence. Energies, tunnel couplings, derivatives, g-tensor elements, and coherence metrics can all shift as the mesh changes. This repository is intended to make that numerical uncertainty explicit and reproducible.

The central idea is to treat mesh refinement as a controlled sequence of approximations rather than as an informal comparison of screenshots. Given an observable Q(h) computed at characteristic mesh scale h, the code can compare coarse, baseline, and fine calculations, quantify absolute and relative shifts, estimate observed convergence order when the mesh ratios permit it, and perform Richardson-style extrapolation for quantities that appear to follow a power-law discretization error.

For three mesh scales h1 > h2 > h3, a simple convergence model is

Q(h) = Q0 + C h^p,

where Q0 is the continuum-limit estimate, C is an unknown coefficient, and p is the observed order. If the refinement ratio is approximately constant, the numerical data can be used to estimate p and then infer an extrapolated Q0. This procedure is only meaningful when the values show interpretable convergence behavior, so the repository exposes diagnostics rather than automatically declaring convergence.

The package includes functions for absolute and relative differences, convergence summaries, observed-order estimates for equal refinement ratios, Richardson extrapolation, and threshold-based pass/fail reports. These tools are intended for quantities such as orbital energies, tunnel coupling, principal g values, Zeeman splittings, susceptibility, T2*, and T1.

Installation is performed with

\`\`\`bash
git clone https://github.com/premathul/GeQubit-Mesh-Convergence-Lab.git
cd GeQubit-Mesh-Convergence-Lab
python -m pip install -e .
\`\`\`

A mesh-convergence claim should always state what observable was tested, how the characteristic mesh scale was defined, what sequence of meshes was used, and what tolerance was accepted. Different observables can converge at very different rates, so convergence of orbital energy does not imply convergence of a derivative or a g-tensor. The long-term goal of this repository is to automate complete numerical uncertainty reports that can accompany quantum-device simulation results.

## Runnable scientific baseline

The script reads three measurements of the same observable at decreasing characteristic spacings. If the successive differences are consistent with a monotone power-law error, it estimates an observed order p from their ratio and extrapolates the finest two values to zero spacing. Because only three points determine both p and the extrapolated limit, the result is a diagnostic rather than a confidence interval. Nonmonotone behavior or a ratio outside the permitted power-law range produces no extrapolation, which is preferable to manufacturing a convergence estimate.

Prepare a CSV with headers `h_nm,value` and three coarse-to-fine rows such as `8,1.16`, `6,1.09`, `4,1.04`; run `python src/main.py mesh.csv`. Every value must represent the same physical state and observable in the same units. Before interpreting a small final shift, check solver tolerances, eigenstate tracking, alignment, domain size, material model, and derivative step sizes. Strongly anisotropic meshes need a documented characteristic spacing or a separate directional refinement study.

## Validation and scope

The calculations in `src/main.py` are transparent baseline models intended for reproducibility and extension. Inputs and assumptions should be reported alongside outputs; numerical agreement with a plotted trace alone does not validate a material-specific prediction. New physical terms should be accompanied by dimensional checks and independent limiting-case comparisons.

## Contact

**Athul Prem** — [GitHub profile](https://github.com/premathul). For scientific discussion or collaboration, open an issue in this repository or reach out through my GitHub profile.
