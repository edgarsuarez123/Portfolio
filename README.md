<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waveBottom&color=0:0d1117,100:1a6dd4&height=220&section=header&text=Edgar%20J.%20Su%C3%A1rez%20Col%C3%B3n&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Software%20Engineer%20%C2%B7%20AI%2FML%20%C2%B7%20Biomedical%20Systems&descSize=18&descAlignY=55&descColor=b0c4de" width="100%" />
</div>

<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=1A6DD4&center=true&vCenter=true&width=620&lines=AI+engineer+who+solves+problems+in+constrained+environments;No+gantry%3F+No+budget%3F+No+staff%3F+Ship+it+anyway.;Defense+%C2%B7+Healthcare+%C2%B7+Biomedical+AI" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <a href="https://linkedin.com/in/edgarjsuarez">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/edgarsuarez123">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</div>

<br/>

I build AI systems that work under real constraints — no gantry, no staff bandwidth, no clean data, no 360° arc. I find the constraint, strip the problem to its core, and ship something that hits a quantitative gate. Defense, healthcare, biomedical — every project below has numbers to back it up.

---

## Featured Projects

### [OneShotXray](https://github.com/edgarsuarez123/OneShotXray) — Freehand X-Ray CT Simulation Pipeline

**Computational proof-of-concept implementing U.S. Patent 12,327,378 B2 (Self-Determined Shot Geometry) for two concurrent SBIR Phase I proposals — Navy ship hull NDT and NIH bedside brain hemorrhage detection. Built in a 5-day sprint.**

- SDSG solver residual **0.084 px** (target < 0.2 px) and **0.077 px** on NIH track — geometry recovered from 2D projections alone, no external tracker
- mART CNR **7.1** on 5mm hemorrhage from a 180° ICU-constrained arc where FBP is completely non-diagnostic (SSIM = 0.013)
- Hemorrhage detection ROC **AUC = 0.92** (target > 0.75) on 10+10 simulated trials
- Full pipeline: physics-based phantom → ASTRA cone_vec projection → Poisson noise → SDSG solver → iterative reconstruction → proposal-quality figures

<div>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" />
</div>

---

### [AF-VNS](https://github.com/edgarsuarez123/AF-VNS) — Closed-Loop AI for Vagus Nerve Stimulation

**Three independent real-time AI pipelines for auricular vagus nerve stimulation — AF/NSR classification, stroke-timed delivery, and tinnitus suppression — sharing a common signal processing core.**

- Tinnitus arousal classifier **AUROC 0.930** (target > 0.80) trained on WESAD; stimulation rate reduced **98.5%** via tri-fold gating
- Stroke pipeline diastole accuracy **84.3%** at **p95 latency 116ms** (target < 200ms) on CVES dataset (228 records)
- AF classification ensemble: CNN + GRU + Transformer over ECG + 7 HRV features; trained on MIT-BIH AF, MIMIC-III, Challenge 2017
- **500+ tests** across all three pipelines; trained on real medical datasets (MIT-BIH AF, MIMIC-III, CVES, WESAD, SHaRe)

<div>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
</div>

---

### [CallCenterAI](https://github.com/edgarsuarez123/CallCenterAI) — HEDIS Outreach Automation Platform

**HIPAA-compliant multi-tenant SaaS that automates HEDIS care-gap outreach for primary care clinics — AI voice calls via Retell AI, outcome logging, and campaign reports with no staff intervention.**

- Projected **$8–16K additional reimbursement per cycle** per clinic by lifting care-gap closure from ~40% to ~80% on 500-patient lists
- **AES-256-GCM** PHI encryption at rest; phones never stored or logged in plaintext; **HMAC-SHA256** webhook verification on all Retell callbacks
- Row-level `clinic_id` scoping on every table and query; Azure deployment with active HIPAA BAA
- Full async FastAPI backend, PostgreSQL 15, Docker, CI, React dashboard, and a 40-page senior-engineer system design report

<div>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" />
</div>

---

### [Clinic Financial Intelligence](https://github.com/edgarsuarez123/clinic-financial-intelligence) — AI-Powered Financial Analytics for Medical Clinics

**Full-stack financial analytics platform with a safe text-to-SQL engine — natural-language queries over clinic revenue data answered with exact DB values, no hallucinated numbers, no arbitrary code execution.**

- Text-to-SQL with an **exact catalog allowlist** (6 reviewed query shapes, read-only role, 5-second statement timeout) — AI cites only values returned from the database
- **209 Python tests + 38 React/Vitest tests**, GitHub Actions CI; **37 Architectural Decision Records**
- 3 least-privilege DB roles, read-only containers, `cap_drop: ALL`, client-side PDF extraction (PHI never transmitted)
- Features: revenue explorer, budget & scenario workspace, staffing cost modeling, multi-insurer breakdowns

<div>
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</div>

---

### [drone_detection](https://github.com/edgarsuarez123/drone_detection) — Real-Time Object Detection with Logging & Analytics

**End-to-end object detection app: YOLOv8 running on live webcam or uploaded video, every detection logged to SQL, analytics dashboard built on top.**

- Configurable confidence threshold and frame-skip rate for CPU/GPU trade-off
- Detections persisted per-source with class, confidence, and bounding box coordinates
- Analytics tab: detections by class (bar) and detections by hour (time-series line chart)

<div>
  <img src="https://img.shields.io/badge/YOLOv8-111111?style=for-the-badge&logo=yolo&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</div>

---

## Tech Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,typescript,react,fastapi,postgres,pytorch,docker,azure,git,linux&theme=dark" />
</div>

---

## GitHub Stats

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=edgarsuarez123&show_icons=true&theme=github_dark&hide_border=true" height="170" />
  <img src="https://streak-stats.demolab.com/?user=edgarsuarez123&theme=github-dark-blue&hide_border=true" height="170" />
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waveTop&color=0:1a6dd4,100:0d1117&height=120&section=footer" width="100%" />
</div>
