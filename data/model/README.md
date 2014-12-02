# Model results

Each file is named `<IC>_<description>.dat` where

- `IC` is the initial condition
  - `glb`: Glauber model
  - `glb-validation`: validation data for Glauber
  - `kln`: KLN model

- `description` denotes what the file contains
  - `cent`: Centrality bins.  Each bin has width 5%; the numbers in the file are the bin middles.
  - `design`: Latin-hypercube design for the input parameters.
  - `params`: Table listing the input parameter labels, TeX-formatted names, min, and max.
  - `mult_<experiment>`: Charged-particle multiplicity with kinematic cuts set to match `<experiment>`.
  - `vn_<experiment>`: Flow cumulant _v<sub>n</sub>_{2} with kinematic cuts set to match `<experiment>`.
    - ALICE kinematic cuts: 0.2 < _p<sub>T</sub>_ < 3.0 GeV, |_η_| < 1.
    - ATLAS kinematic cuts: 0.5 < _p<sub>T</sub>_ < 20.0 GeV, |_η_| < 2.5.

The design is repeated for each centrality bin.  The _minimum_ number of events for each centrality bin and
design point is

Centrality bin | Minimum events
-------------- | --------------
0–5%           | 1500
10–15%         | 2000
20–25%         | 2500
30–35%         | 3000
40–45%         | 3500
50–55%         | 4000

In the `design` file, columns correspond to input parameters (as listed in `params`) and rows to design
points.

In files `mult` and `vn`, columns correspond to centrality bins (as listed in `cent`) and rows to design
points.
