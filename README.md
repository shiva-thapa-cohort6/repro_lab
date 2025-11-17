
# Reproducible Mini-Analysis (Week 3 – Part 3)

**Synopsis:** Computes average time-to-triage and correct triage coverage from a small synthetic incident dataset, and writes results to `docs/`.

## Project Structure
```
README.md
/src/    # code for the one-step analysis
/data/   # small synthetic input
/docs/   # run logs or figures
.gitignore
Dockerfile
```

## Reproduce this (one command)
```bash
docker build -t reproducibility-lab . && docker run --rm -v "$PWD":/work reproducibility-lab
```

## What you should see
- Console line similar to: `MTTT=**s; Coverage=**% -> wrote metric.txt and chart.png in docs/`
- File `docs/metric.txt` containing two lines:
  - `Average time-to-triage (seconds) = <value>`
  - `Correct triage coverage (%) = <value>`
- Image `docs/chart.png` (histogram).

## Data Note
Synthetic data approximates triage timing and correctness while protecting restricted production data.

## Standards Note (optional)
NIST CSF 2.0 GV.ME-01 — “Measurement and performance management are conducted to assess cybersecurity posture.” (p. 20)



## Standards Note

This project connects parts of its analysis process with the NIST Cybersecurity Framework 2.0 and NIST SP 800-207 Zero Trust Architecture [3], [4]. The Standards Crosswalk in `docs/crosswalk.md` links important components to CSF Outcomes ID.RA-01, PR.PS-01, and PR.PS-04, and to Zero Trust Tenets 2 and 5. Evidence for these mappings is found in the container and environment files (`Dockerfile`, `requirements.txt`), the analysis script (`src/run.py`), and the recorded results (`docs/metric.txt`, `docs/log.txt`, `docs/chart.png`). Together, this note and the crosswalk file show how the project aligns with the referenced standards.
