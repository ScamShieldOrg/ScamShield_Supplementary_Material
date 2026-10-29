# ScamShield-VN: Verbatim Forensic System Prompts & Output Schemas

This directory provides the complete, verbatim system instructions, in-context exemplars, and privacy sanitization schemas evaluated in:
* **"ScamShield-VN: Evidence-Driven Two-Tier Architecture for Vietnamese Scam and Phishing Detection"** (JAIT / ICIIT 2027).

---

## Directory Contents

| File | Role / Configuration | Target LLM | Purpose |
| :--- | :--- | :--- | :--- |
| `gemini_3.5_flash_5shot_icl.yaml` | Baseline B3 | Gemini 3.5 Flash | 5-Shot in-context learning baseline prompt with 5 balanced exemplars. |
| `p_single_forensic_prompt.yaml` | Baseline P-single (Wang et al., ACL 2024) | GPT-6.1-sol | Solitary LLM structured prompt evaluating 5 forensic threat axes. |
| `tier2_council_3agent_prompts.yaml` | Proposed Arm 2 | Multi-Provider (GPT-6.1-sol, Gemini 3.5/3.8) | Consolidated 3-agent council (Cyber-Bank, Psycho-Teencode, Public Defender). |
| `tier2_council_5agent_prompts.yaml` | Reference Arm 1 | Multi-Provider | 5 decoupled specialist personas. |
| `pii_sanitizer_regex_rules.json` | Privacy Pre-processor | Local Client Regex | Article 25 Decree 13/2023/ND-CP client-side regex rules. |
