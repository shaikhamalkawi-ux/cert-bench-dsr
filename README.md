# CERT-Bench: Decision-Stability Radius (DSR)

Research reproducibility materials for decision-specific task-weight sensitivity in multi-task AI model selection.

## Scope of this repository

The current release is a **limited, evidence-gated reproducibility snapshot** associated with the frozen R15 research baseline. The uploaded archive contains:

- Machine-readable summary tables for TabArena, BenchPress, and BeyondArena.
- Derived Tetouan electricity-demand model-selection inputs and sensitivity outputs.
- A deterministic Python script for the Tetouan calculations.
- An SHA-256 manifest and a saved successful execution log.

**Important:** The three benchmark summaries are not full benchmark source matrices. This archive alone does **not** rerun every benchmark calculation or reconstruct all 109 pairwise certificates from raw source artifacts. The Tetouan case is a retrospective analysis of published forecasting tables, not model retraining or a live deployment.

## Reproduce the Tetouan calculation

Download `artifacts/CERT_Bench_ESWA_R15_Anonymous_Reproducibility_Package.zip` and extract it.

Requirements: Python 3, NumPy, pandas, and SciPy. From the extracted folder:

```bash
python -m pip install numpy pandas scipy
python reproduce_tetouan_sensitivity.py
```

Expected output begins with `PASS`; the script also prints the decision-stability radii and sensitivity diagnostics. Validate file integrity against `SHA256SUMS.txt` after extracting.

The exact archived ZIP has SHA-256:

```
19f894d6e0772e3971eb26c5ca91cc796955ffa9c9b5ca647cd65e609e30163e
```

## Data provenance and interpretation

Tetouan load-share inputs and published forecasting scores are secondary transcriptions, including results described by Biswas et al. (2026), *Results in Engineering*, DOI [10.1016/j.rineng.2026.110289](https://doi.org/10.1016/j.rineng.2026.110289). The public Tetouan power-consumption dataset has DOI [10.24432/C5B034](https://doi.org/10.24432/C5B034).

The decision-stability radius (DSR) is computed with the admitted score matrix fixed. Sensitivity to changes in task weights is not sampling uncertainty. The published-MAPE rounding range is **not a confidence interval**.

Third-party full benchmark data are not included when redistribution permission is unclear. Please consult the original benchmark sources.

## Version and publication status

- Frozen research baseline: **R15**.
- This repository currently contains only the restricted-scope reproducibility material, **not** the identifiable manuscript or submission correspondence.
- This GitHub repository is owner-identifying and should **not** be represented as an anonymous reviewer repository.
- No public Zenodo DOI has been assigned here.

## License

No license has yet been assigned to this repository. Do not assume that third-party data, transcribed source tables, or other materials are licensed for unrestricted redistribution.
