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

## Contact

**Athul Prem**

For scientific discussion, collaboration, or suggestions related to this project, please contact Athul Prem through the GitHub account associated with this repository.
