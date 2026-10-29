# ScamShield-VN: Supplementary Material & Technical Appendix

[![Open Science](https://img.shields.io/badge/Open%20Science-Replication%20Artifacts-blue.svg)](https://github.com/thalord2825/ScamShield_Supplementary_Material)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Format: CSV%20%7C%20MD%20%7C%20LaTeX](https://img.shields.io/badge/Formats-CSV%20%7C%20MD%20%7C%20LaTeX-orange.svg)](#supplementary-tables-index)

This repository serves as the official **Supplementary Material, Technical Appendix, and Open Science Replication Archive** for the academic research manuscript:

> **"ScamShield-VN: Evidence-Driven Two-Tier Architecture for Vietnamese Scam and Phishing Detection"**  
> *Target Venue:* Journal of Advances in Information Technology (JAIT) / 12th International Conference on Intelligent Information Technology (ICIIT 2027)  
> *Authors:* Nguyen Trung Hieu, Nguyen Minh Quang, Hoang Hai Phuc, Phan Tran Hoang Tran, Nguyen Quoc Huy, and Le Thi Quynh Chi  
> *Affiliation:* Department of Software Engineering, FPT University, Ho Chi Minh City, Vietnam  
> *Primary Repository:* [https://github.com/QuangWorkIT/RBL_ScamShield](https://github.com/QuangWorkIT/RBL_ScamShield)

---

## 📁 Repository Organization

```text
ScamShield_Supplementary_Material/
├── README.md                           # This comprehensive guide and artifact index
├── LICENSE                             # MIT Open Source License
├── tables/                             # Supplementary Tables S1 - S7 (CSV, Markdown, LaTeX)
│   ├── Table_S1_literature_overview.{csv,md,tex}
│   ├── Table_S2_model_specifications.{csv,md,tex}
│   ├── Table_S3_confusion_matrices_2x3.{csv,md,tex}
│   ├── Table_S4_threshold_sensitivity_sweeps.{csv,md,tex}
│   ├── Table_S5_dataset_partitions_breakdown.{csv,md,tex}
│   ├── Table_S6_mcnemar_statistical_tests.{csv,md,tex}
│   └── Table_S7_multiseed_benchmark_5runs.{csv,md,tex}
├── prompts/                            # Verbatim prompt templates & privacy schemas
│   ├── README.md
│   ├── gemini_3.5_flash_5shot_icl.yaml
│   ├── p_single_forensic_prompt.yaml
│   ├── tier2_council_3agent_prompts.yaml
│   ├── tier2_council_5agent_prompts.yaml
│   └── pii_sanitizer_regex_rules.json
├── latex/                              # Standalone LaTeX source for Supplementary PDF
│   ├── supplementary.tex
│   └── references.bib
└── scripts/                            # Integrity verification and invariant tests
    └── verify_supplementary_invariants.py
```

---

## 📊 Supplementary Tables Index

All empirical tables from the research paper are cross-referenced and provided in three machine-readable formats (**CSV**, **Markdown**, and **LaTeX**):

| Table | Scientific Subject | Data Sample Size | Key Metrics / Findings | Direct Links |
| :--- | :--- | :--- | :--- | :--- |
| **Table S1** | **Comparative Literature Overview** | 6 foundational studies | Contrasts ScamShield-VN against PhoBERT, MLTEA, VNSED, FraudSMSWalker, QuishingShield, and EdgeAI. | [CSV](tables/Table_S1_literature_overview.csv) \| [MD](tables/Table_S1_literature_overview.md) \| [TeX](tables/Table_S1_literature_overview.tex) |
| **Table S2** | **Model Specifications & API Cards** | 10 evaluated models | Documenting runtime, temperature, context, and circuit-breaker standby chains across Tier 1 and Tier 2 arms. | [CSV](tables/Table_S2_model_specifications.csv) \| [MD](tables/Table_S2_model_specifications.md) \| [TeX](tables/Table_S2_model_specifications.tex) |
| **Table S3** | **$2 \times 3$ Confusion Matrices** | $N=117$ Hard Forensic Suite | Verdict accounting across `SCAM-RISK`, `LOW-RISK`, `UNKNOWN`; verifies $0.00\%$ FPR on authentic banking OTPs. | [CSV](tables/Table_S3_confusion_matrices_2x3.csv) \| [MD](tables/Table_S3_confusion_matrices_2x3.md) \| [TeX](tables/Table_S3_confusion_matrices_2x3.tex) |
| **Table S4** | **Routing Threshold Sweeps ($\tau$)** | $N=384$ Combined Suite | Sensitivity profiling across $\tau \in [0.70, 0.95]$; confirms Pareto-optimal operating threshold $\tau=0.90$. | [CSV](tables/Table_S4_threshold_sensitivity_sweeps.csv) \| [MD](tables/Table_S4_threshold_sensitivity_sweeps.md) \| [TeX](tables/Table_S4_threshold_sensitivity_sweeps.tex) |
| **Table S5** | **Corpus Partition Breakdown** | $N=2,664$ Unified Corpus | Class balance across Train ($N=2,397$), Frozen Test ($N=267$), Hard Forensic ($N=117$), and Dev ($N=384$). | [CSV](tables/Table_S5_dataset_partitions_breakdown.csv) \| [MD](tables/Table_S5_dataset_partitions_breakdown.md) \| [TeX](tables/Table_S5_dataset_partitions_breakdown.tex) |
| **Table S6** | **Paired McNemar Hypothesis Tests** | $N=267$ and $N=117$ | Panel A: ViSoBERT vs. Gemini ($p < 0.0001, \text{OR}=11.00$). Panel B: 3-Agent vs. 5-Agent ($p=0.0625$). | [CSV](tables/Table_S6_mcnemar_statistical_tests.csv) \| [MD](tables/Table_S6_mcnemar_statistical_tests.md) \| [TeX](tables/Table_S6_mcnemar_statistical_tests.tex) |
| **Table S7** | **Multi-Seed 5-Run Benchmark** | $K=5$ Training Seeds | Mean scam recall $95.64\% \pm 2.04\%$, Macro-F1 $94.51\% \pm 0.96\%$; Frozen holdout recall $96.00\%$ ($72/75$). | [CSV](tables/Table_S7_multiseed_benchmark_5runs.csv) \| [MD](tables/Table_S7_multiseed_benchmark_5runs.md) \| [TeX](tables/Table_S7_multiseed_benchmark_5runs.tex) |

---

## 🛡️ Verbatim Forensic Prompts & Privacy Safeguards

The [`prompts/`](prompts/) directory archives full unedited instructions and schemas:
1. **Gemini 3.5 Flash 5-Shot ICL Prompt:** Strict integer output instruction (`0` or `1`) with balanced exemplars.
2. **P-single Structured Forensic Prompt:** Solitary LLM prompt covering five forensic threat axes (Technical IOCs, Psychological urgency, Linguistic evasion, Financial regulations, Transaction safeguards).
3. **Consolidated 3-Agent Council Prompts (Arm 2):**
   - *Seat A:* Cyber-Financial & Banking Security Analyst (`ROLE_CYBER_BANK`, weight $1.3$).
   - *Seat B:* Psycholinguistic & Vietnamese Slang Profiler (`ROLE_PSYCHO_TEENCODE`, weight $1.2$).
   - *Seat C:* Public Defender & Anti-False-Positive Advocate (`ROLE_DEFENDER`, weight $1.3$, veto boost $\delta = -0.25$).
4. **Reference 5-Agent Council Prompts (Arm 1):** Five decoupled specialist personas.
5. **Client-Side Regex Sanitizer (Decree 13/2023/ND-CP Article 25):** Redacts Vietnamese mobile numbers, bank accounts, citizen IDs (CCCD), OTP verification tokens, and balance amounts prior to off-device escalation.

---

## 🔬 Reproducibility Verification

To automatically verify that all 21 table files conform to exact sample totals ($N=117, N=267, N=384, N=2,664$), mathematical consistency, and valid YAML/JSON prompt syntax, execute:

```bash
python scripts/verify_supplementary_invariants.py
```

Expected output:
```text
[TEST 1] Verifying presence of all 7 Supplementary Tables in CSV, MD, and TEX...
  --> PASS: All 21 table artifacts exist and are non-empty.
[TEST 2] Verifying Table S3 (2x3 Confusion Matrix) Invariants...
  --> PASS: Table S3 totals match N_scam=98, N_benign=19, Total=117 with exact abstentions.
[TEST 3] Verifying Table S4 (Threshold Sensitivity) Invariants...
  --> PASS: Table S4 monotonic escalation and accuracy verified.
[TEST 4] Verifying Table S5 (Corpus Breakdown) Invariants...
  --> PASS: Table S5 class balance and sample sizes verified.
[TEST 5] Verifying Prompt configurations and PII Sanitizer...
  --> PASS: All prompt files and PII regex rules parsed successfully.

[ALL INVARIANT TESTS PASSED SUCCESSFULLY!]
```

---

## 📜 Citation

If you use these supplementary materials, tables, or prompt architectures in your research, please cite our paper:

```bibtex
@article{scamshield_vn_2027,
  author    = {Nguyen Trung Hieu and Nguyen Minh Quang and Hoang Hai Phuc and Phan Tran Hoang Tran and Nguyen Quoc Huy and Le Thi Quynh Chi},
  title     = {{ScamShield-VN: Evidence-Driven Two-Tier Architecture for Vietnamese Scam and Phishing Detection}},
  journal   = {Journal of Advances in Information Technology},
  year      = {2027},
  note      = {Supplementary repository: \url{https://github.com/thalord2825/ScamShield_Supplementary_Material}}
}
```
