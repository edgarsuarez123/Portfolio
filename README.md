<h1 align="center">Edgar J. Suárez Colón</h1>

<p align="center">
  <strong>AI Engineer</strong> &nbsp;·&nbsp; Defense &nbsp;·&nbsp; Healthcare &nbsp;·&nbsp; Biomedical Systems
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/edgar-suarez-colon-35861124a">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://github.com/edgarsuarez123">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" />
  </a>
</p>

<br>

I build AI for environments where the standard assumptions break — no gantry, no clean data, no full sensor access, no staff bandwidth. Every project below has a quantitative acceptance gate and hits it.

---

## Projects

### [OneShotXray](https://github.com/edgarsuarez123/OneShotXray) &nbsp;—&nbsp; Freehand X-Ray CT

Standard CT requires a precision gantry. This doesn't. Implementation of U.S. Patent 12,327,378 B2 (Self-Determined Shot Geometry) for two SBIR Phase I proposals: Navy ship hull NDT and NIH bedside brain hemorrhage monitoring in the ICU. Built from scratch in 5 days.

| Track | Metric | Target | Result |
|---|---|---|---|
| Navy | SDSG solver residual | < 0.2 px | **0.084 px** |
| NIH | mART CNR @ 5mm hemorrhage | ≥ 4.0 | **7.1** |
| NIH | Hemorrhage ROC AUC | > 0.75 | **0.92** |

FBP on a 180° ICU-constrained arc is non-diagnostic (SSIM = 0.013). mART on the same data hits CNR 7.1. That gap is the whole argument.

`Python` `ASTRA Toolbox` `CUDA` `NumPy` `SciPy` `h5py`

---

### [AF-VNS](https://github.com/edgarsuarez123/AF-VNS) &nbsp;—&nbsp; Closed-Loop AI for Vagus Nerve Stimulation

Three independent real-time pipelines for auricular vagus nerve stimulation — AF/NSR classification, stroke-timed delivery (diastole + exhalation gate), and tinnitus suppression (tri-fold: cardiac + respiratory + arousal). Shared signal processing core, hardware-grade latency targets.

- Tinnitus arousal classifier AUROC **0.930** on WESAD (target > 0.80); tri-fold gating cut stimulation rate by **98.5%**
- Stroke pipeline diastole accuracy **84.3%**, p95 latency **116ms** on CVES (228 records)
- AF ensemble: CNN + GRU + Transformer over ECG + 7 HRV features; trained on MIT-BIH AF, MIMIC-III, Challenge 2017
- 500+ tests across all three pipelines

`Python` `PyTorch` `scikit-learn` `neurokit2` `GBT`

---

### [CallCenterAI](https://github.com/edgarsuarez123/CallCenterAI) &nbsp;—&nbsp; HEDIS Outreach Platform

Primary care clinics receive monthly HEDIS care-gap lists but don't have staff bandwidth to work them. This SaaS places the calls via Retell AI, records outcomes, and generates reports — no staff intervention. Built HIPAA-compliant from the ground up.

- AES-256-GCM PHI encryption at rest; HMAC-SHA256 on all webhooks; Azure deployment with active BAA
- Multi-tenant with row-level `clinic_id` isolation on every query
- Closing 40% → 80% of gaps on a 500-patient list = **$8–16K additional reimbursement per cycle**
- Async FastAPI + PostgreSQL 15 + Docker + React dashboard + 40-page system design report

`FastAPI` `PostgreSQL` `SQLAlchemy async` `Docker` `Azure` `Retell AI`

---

### [Clinic Financial Intelligence](https://github.com/edgarsuarez123/clinic-financial-intelligence) &nbsp;—&nbsp; Financial Analytics + Text-to-SQL

Revenue tracking, provider cost analysis, staffing simulations, and natural-language queries over clinic financial data — without arbitrary code execution or hallucinated numbers.

- Text-to-SQL with an exact catalog allowlist: 6 reviewed query shapes, read-only DB role, 5s statement timeout. AI cites only values returned from the database.
- 209 Python + 38 React/Vitest tests; 37 Architectural Decision Records; GitHub Actions CI
- 3 least-privilege DB roles, read-only containers, `cap_drop: ALL`, client-side PDF extraction

`React 19` `TypeScript` `FastAPI` `PostgreSQL 17` `Ollama` `Docker`

---

### [drone_detection](https://github.com/edgarsuarez123/drone_detection) &nbsp;—&nbsp; Real-Time Detection with Persistence

YOLOv8 on live webcam or uploaded video — every detection (class, confidence, bounding box, source) written to SQL as it happens. Analytics tab shows detections by class and detection rate over time. Configurable confidence threshold and frame-skip for CPU/GPU trade-off.

`YOLOv8` `Streamlit` `OpenCV` `SQLAlchemy` `Plotly`

---

## Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,typescript,react,fastapi,postgres,docker,azure,git,linux&theme=dark" />
</div>

---

## Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=edgarsuarez123&show_icons=true&theme=github_dark&hide_border=true&rank_icon=github" height="160" />
  <img src="https://streak-stats.demolab.com/?user=edgarsuarez123&theme=github-dark-blue&hide_border=true" height="160" />
</div>
