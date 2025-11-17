
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

This capstone repository incorporates selected elements of the NIST Cybersecurity Framework (CSF) 2.0 and NIST SP 800-207 Zero Trust Architecture [3], [4]. The Standards Crosswalk in `docs/crosswalk.md` maps three key project components—container configuration, the analysis script, and stored log outputs—to CSF Outcomes PR.PS-01, PR.PS-04, and ID.RA-01, and to Zero Trust Tenets 2 and 5.

Evidence supporting these mappings is included in:
- Container and environment definitions: `Dockerfile`, `requirements.txt`
- Analysis workflow: `src/run.py`
- Logged outputs and visual artifacts: `docs/metric.txt`, `docs/log.txt`, `docs/chart.png`
- Standards mapping and profile snippet: `docs/crosswalk.md`

This note provides traceability between the reproducible workflow developed in Homework 11 and the standards alignment required in Homework 12.

