### Quantifying properties of hot and dense QCD matter through systematic model-to-data comparison

[arXiv:1502.00339 [nucl-th]](http://arxiv.org/abs/1502.00339)

This repository contains all relevant code and data for the above paper.
In principle, anyone can completely reproduce the results:

1. Requirements: Python 3 with numpy, scipy, matplotlib, [emcee](http://dan.iel.fm/emcee), [george](http://dan.iel.fm/george), and my custom library [mtd](https://github.com/jbernhard/mtd).
2. Run the `preprocess` scripts in `data/exp` and `data/model`.
3. Run the emulator+MCMC analysis.
   Unless you have a very fast CPU, a lot of memory, and scipy compiled with Intel MKL, it will probably take prohibitively long to reproduce the level of statistics in the paper.
   Edit `mcmc/train-and-calibrate` on line 163 to reduce the number of MCMC steps; try `nwalkers=100, nsteps=1000, nburnsteps=500`.
   Then run `./train-and-calibrate glb` to perform the analysis for the Glauber model and once again `./train-and-calibrate kln` for KLN.
4. Generate plots and tables with `make-plots` in `fig`.
5. Compile the PDF normally.

Alternatively, feel free to contact me for the original high-statistics MCMC data.
