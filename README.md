
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
