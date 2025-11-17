# Standards Crosswalk – CYBR 698 Capstone (Homework 12)

## 3.1 Standards Crosswalk Table

The table below links three essential scope elements from the Homework 11 / capstone repository—method, repo, and workflow—to specific NIST CSF 2.0 Outcomes and Zero Trust Architecture (ZTA) principles. Evidence paths reference exact files in the repository. The CSF details were derived from NIST CSWP 29 and The NIST Cybersecurity Framework (CSF) 2.0 [3], while the Zero Trust principles were taken from NIST SP 800-207, Zero Trust Architecture [4].

| **Scope Element** | **CSF 2.0 Outcome (Exact Text + Page)** | **ZTA Tenet (Exact Text + Page)** | **ISO 27001 Theme** | **Evidence Pointer** | **Rationale (100–150 words)** |
|------------------|------------------------------------------|-----------------------------------|----------------------|------------------------|--------------------------------|
| **Containerized reproducible workflow (Dockerfile + analysis script)** | **PR.PS-01:** Configuration management practices are established and applied. (CSF 2.0, p. 21) [3] | “**All communication is secured regardless of network location.**” (ZTA Tenet 2, p. 7) [4] | Technological | `Dockerfile`, `requirements.txt`, `src/run.py`, `README.md` | The containerized workflow provides a controlled, consistent environment for running the analysis, which aligns with PR.PS-01. All dependencies, runtime versions, and execution steps are defined as code, reducing drift and ensuring that the analysis runs the same way each time [3]. The design reflects Zero Trust Tenet 2 because it avoids implicit trust in the host system or network; instead, the container enforces its own bounded runtime configuration regardless of where it is executed [4]. This approach supports structured configuration management and provides a foundation for stronger technical hardening as the project matures. |
| **One-step analysis script generating metrics and logs** | **ID.RA-01:** Vulnerabilities in assets are identified, validated, and recorded. (CSF 2.0, p. 19) [3] | “**The enterprise monitors and measures the integrity and security posture of all owned and associated assets.**” (ZTA Tenet 5, p. 7) [4] | Technological | `src/run.py`, `data/`, `docs/metric.txt`, `docs/log.txt` | The analysis script handles sample data and produces consistent results and logs. This matches ID.RA-01’s goal of identifying and recording important security information in a repeatable way [3]. Each execution creates measurable evidence—such as metrics and log entries—that shows how the analysis behaved. This supports Zero Trust Tenet 5 by enabling regular checks of integrity and posture, because repeated runs can be compared to identify anomalies or unexpected changes [4]. The saved outputs also establish an audit trail that strengthens accountability and enhances monitoring as the capstone develops. |
| **Logging and output artifacts stored in `/docs`** | **PR.PS-04:** Log records are generated and made available for continuous monitoring. (CSF 2.0, p. 21) [3] | “**The enterprise monitors and measures the integrity and security posture of all owned and associated assets.**” (ZTA Tenet 5, p. 7) [4] | Technological / Organizational | `docs/metric.txt`, `docs/log.txt`, `docs/chart.png` | The project systematically produces log files and output artifacts for each analysis run and stores them under version control. This aligns with PR.PS-04, which emphasizes generating and maintaining log records to support continuous monitoring [3]. These artifacts provide insight into execution behavior, results produced, and whether the workflow operated as expected. The practice supports Zero Trust Tenet 5 by enabling ongoing assessment of posture through observable and quantifiable data [4]. Maintaining these files in the repository enhances documentation governance, supports trend analysis, and establishes a strong foundation for adding automated checks or additional controls in future stages of the capstone. |

---

## 3.2 Profile Snippet (Current → Target Profile)

The following bullets apply the Current/Target Profile concept from NIST SP 1301, which describes how organizations compare their present implementation of CSF Outcomes against a desired future state [5].

**Current Profile (SP 1301 terminology)** —  
For PR.PS-01, PR.PS-04, and ID.RA-01, the project currently demonstrates foundational implementation. Configuration is defined through a container and dependency files, logs and metrics are generated consistently, and the analysis script runs reliably on sample data. However, reviews of configuration, logs, and outputs are informal and not yet part of an established process.

**Target Profile (SP 1301 terminology)** —  
By the end of the capstone, these same Outcomes will be implemented more formally. Configuration changes for PR.PS-01 will be reviewed and documented; log and metric outputs for PR.PS-04 will be routinely evaluated; and execution and interpretation of analysis results for ID.RA-01 will follow clearer criteria. This reflects SP 1301’s guidance for maturing from a basic Current Profile to an improved Target Profile [5].

---

## 3.3 Standards Note (for README.md)

This text is designed for direct inclusion in the project README to fulfill the “Standards Note” requirement while maintaining traceability.

**Standards Note**  
This project connects parts of its analysis process with the NIST Cybersecurity Framework 2.0 and NIST SP 800-207 Zero Trust Architecture [3], [4]. The Standards Crosswalk in `docs/crosswalk.md` links important components to CSF Outcomes ID.RA-01, PR.PS-01, and PR.PS-04, and to Zero Trust Tenets 2 and 5. Evidence for these mappings is found in the container and environment files (`Dockerfile`, `requirements.txt`), the analysis script (`src/run.py`), and the recorded results (`docs/metric.txt`, `docs/log.txt`, `docs/chart.png`). Together, this note and the crosswalk file show how the project aligns with the referenced standards.
