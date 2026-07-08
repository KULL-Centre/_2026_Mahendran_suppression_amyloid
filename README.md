## Association between phase-separation propensity and LARKS fraction in human IDRs

The repository contains the code and data to analyze the association between predicted phase-separation propensity and LARKS fraction in human IDRs.

### Layout
- `LARKS_analysis.ipynb` reproduces Fig. 6k and S13
- `data` contains matches between entries in the IDRome [1] and LARKS databases [2] 
- `find_LARKS.py` is a Python script that maps LARKS database entries to IDRome sequences and computes the LARKS fraction for each IDR
- `IDRome_DB_PSpred.csv` contains IDRome sequences together with phase-separation predictions obtained from a machine-learning model trained on CALVADOS simulation data [3]. The machine-learning model and related code are available at [github.com/KULL-Centre/\_2024\_buelow\_PSpred](https://github.com/KULL-Centre/_2024_buelow_PSpred).

### Usage

To open the Notebook, install [Miniconda](https://conda.io/miniconda.html) and make sure all required packages are installed by issuing the following terminal commands

```bash
    conda env create -f environment.yml
    conda activate idrome
    jupyter-notebook
```

### References

1. Hughes, M. P., Goldschmidt, L. & Eisenberg, D. S. *Prevalence and species distribution of the low-complexity, amyloid-like, reversible, kinked segment structural motif in amyloid-like fibrils*. *Journal of Biological Chemistry* **297**, 101194. https://doi.org/10.1016/j.jbc.2021.101194 (2021).

2. Tesei, G., Trolle, A. I. *et al.* *Conformational ensembles of the human intrinsically disordered proteome*. *Nature* **626**, 897–904. https://doi.org/10.1038/s41586-023-07004-5 (2024).

3. von Bülow, S., Tesei, G., Zaidi, F. K., Mittag, T. & Lindorff-Larsen, K. *Prediction of phase-separation propensities of disordered proteins from sequence*. *Proceedings of the National Academy of Sciences* **122**, e2417920122. https://doi.org/10.1073/pnas.2417920122 (2025).
