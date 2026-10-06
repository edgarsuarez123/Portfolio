# Edgar J. Suárez Colón

**Software Engineer · AI/ML · Biomedical Systems**
U.S. Air Force Palace Acquire (PAQ) Program · Incoming May 2026
B.S. Computer Engineering, University of Puerto Rico – Mayagüez

[GitHub](https://github.com/edgarsuarez123) · [LinkedIn](https://linkedin.com/in/edgarjsuarez)

---

## Projects

### [OneShotXray](https://github.com/edgarsuarez123/OneShotXray) — Freehand X-Ray CT Simulation Pipeline

> Computational preliminary data for two concurrent SBIR Phase I proposals implementing U.S. Patent 12,327,378 B2 (Self-Determined Shot Geometry). Built in a 5-day sprint.

Two tracks — Navy ship hull NDT (200 keV steel) and NIH bedside brain hemorrhage CT (70 keV, ICU-constrained 180° arc). Complete pipeline from physics-based phantom generation → forward projection → SDSG geometry recovery → iterative reconstruction → quantitative figures.

| Track | Gate | Target | Achieved |
|-------|------|--------|----------|
| Navy | SDSG solver residual | < 0.2 px | **0.084 px** |
| Navy | mART CNR @ 0.8mm crack | ≥ 4.0 | **> 4.0** |
| NIH | SDSG solver residual | < 0.3 px | **0.077 px** |
| NIH | mART CNR @ 5mm hemorrhage | ≥ 4.0 | **7.1** |
| NIH | ROC AUC — hemorrhage detection | > 0.75 | **0.92** |

**Stack:** Python 3.11 · ASTRA Toolbox 2.4.1 (CUDA) · NumPy · SciPy · scikit-image · h5py · matplotlib

---

### [CallCenterAI](https://github.com/edgarsuarez123/CallCenterAI) — HEDIS Outreach Automation Platform

> Multi-tenant SaaS that automates HEDIS care-gap outreach for primary care clinics. Clinics upload a patient CSV; the system places AI voice calls via Retell AI, records outcomes, and generates reports — without staff intervention.

- **HIPAA-compliant** — AES-256-GCM PHI encryption at rest, phones masked in all logs, HMAC-SHA256 webhook verification
- **Multi-tenant** — row-level `clinic_id` scoping on every table and query
- **Business impact** — automating outreach from 40% → 80% gap closure on 500 patients = $8–16K additional reimbursement per cycle
- Full async FastAPI backend, PostgreSQL, Docker, CI, React dashboard, and a senior-engineer system design report

**Stack:** FastAPI · PostgreSQL 15 · SQLAlchemy 2.0 async · AES-256-GCM · Retell AI · Docker · Azure (HIPAA BAA)

---

### [Clinic Financial Intelligence](https://github.com/edgarsuarez123/clinic-financial-intelligence) — AI-Powered Financial Analytics for Medical Clinics

> Full-stack platform for clinic revenue tracking, provider cost analysis, staffing budget simulations, and natural-language financial queries — answered safely without arbitrary code execution.

- **Ask Clarity** — text-to-SQL with an exact catalog allowlist (6 reviewed query shapes); AI cites only values returned from the DB, never invents numbers
- **209 Python tests + 38 React/Vitest tests**, GitHub Actions CI
- **37 Architectural Decision Records** documenting every major design choice
- 3 least-privilege DB roles, read-only containers, `cap_drop: ALL`, client-side PDF extraction (PHI never transmitted)

**Stack:** React 19 · TypeScript · FastAPI · PostgreSQL 17 · Ollama (local LLM) · Docker · nginx

---

### [AF-VNS](https://github.com/edgarsuarez123/AF-VNS) — Closed-Loop AI for Vagus Nerve Stimulation

> Three independent real-time AI pipelines for auricular vagus nerve stimulation — sharing a common signal processing core and closed-loop inference architecture.

| Pipeline | Signals | Key Result |
|----------|---------|------------|
| AF vs NSR classification | ECG + HRV | CNN + GRU + Transformer ensemble, AUROC target ≥ 0.75 |
| Stroke bifold closed-loop VNS | ECG | Diastole accuracy 84.3%, p95 latency **116ms** |
| Tinnitus tri-fold closed-loop VNS | PPG + EDA | Arousal classifier AUROC **0.930**, stim rate reduced 98.5% |

- Trained on MIT-BIH AF, MIMIC-III, CVES, WESAD, and SHaRe datasets
- 500+ tests across all three pipelines

**Stack:** Python · PyTorch · neurokit2 · scikit-learn · GBT

---

### [Drone Detection](https://github.com/edgarsuarez123/drone_detection) — Real-Time Object Detection with Analytics

> Streamlit app running YOLOv8 on live webcam or uploaded video, logging every detection to a SQL database with an analytics dashboard (detections by class and by hour).

**Stack:** YOLOv8 · Streamlit · OpenCV · SQLAlchemy · Plotly

---

## Skills

**Languages:** Python · TypeScript · JavaScript · C++ · Java · SQL
**AI/ML:** PyTorch · ASTRA Toolbox · scikit-learn · YOLOv8 · Transformer architectures · text-to-SQL
**Backend:** FastAPI · SQLAlchemy · PostgreSQL · Docker · Alembic · asyncio
**Frontend:** React 19 · Vite · Recharts
**Security:** AES-256-GCM · HIPAA compliance · HMAC · least-privilege DB roles
**Other:** CUDA · Git · GitHub Actions · Azure · Streamlit
