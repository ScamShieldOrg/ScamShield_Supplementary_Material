import os
import sys
import csv
import json
import yaml

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)
TABLES_DIR = os.path.join(REPO_DIR, "tables")
PROMPTS_DIR = os.path.join(REPO_DIR, "prompts")

def test_tables_exist():
    print("[TEST 1] Verifying presence of all 7 Supplementary Tables in CSV, MD, and TEX...")
    expected_tables = [
        "Table_S1_literature_overview",
        "Table_S2_model_specifications",
        "Table_S3_confusion_matrices_2x3",
        "Table_S4_threshold_sensitivity_sweeps",
        "Table_S5_dataset_partitions_breakdown",
        "Table_S6_mcnemar_statistical_tests",
        "Table_S7_multiseed_benchmark_5runs"
    ]
    for tbl in expected_tables:
        for ext in [".csv", ".md", ".tex"]:
            path = os.path.join(TABLES_DIR, f"{tbl}{ext}")
            assert os.path.exists(path), f"Missing table artifact: {path}"
            assert os.path.getsize(path) > 50, f"Table artifact too small/empty: {path}"
    print("  --> PASS: All 21 table artifacts exist and are non-empty.")

def test_s3_confusion_invariants():
    print("[TEST 2] Verifying Table S3 (2x3 Confusion Matrix) Invariants...")
    s3_path = os.path.join(TABLES_DIR, "Table_S3_confusion_matrices_2x3.csv")
    with open(s3_path, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    rows = reader[1:]
    for r in rows:
        cfg = r[0]
        s_scam = int(r[1])
        s_low = int(r[2])
        s_unk = int(r[3])
        b_scam = int(r[4])
        b_low = int(r[5])
        b_unk = int(r[6])
        total_abst = int(r[9])

        scam_total = s_scam + s_low + s_unk
        benign_total = b_scam + b_low + b_unk
        assert scam_total == 98, f"Row {cfg}: Scam total {scam_total} != 98"
        assert benign_total == 19, f"Row {cfg}: Benign total {benign_total} != 19"
        assert (s_unk + b_unk) == total_abst, f"Row {cfg}: Abstention mismatch"
    print("  --> PASS: Table S3 totals match N_scam=98, N_benign=19, Total=117 with exact abstentions.")

def test_s4_threshold_invariants():
    print("[TEST 3] Verifying Table S4 (Threshold Sensitivity) Invariants...")
    s4_path = os.path.join(TABLES_DIR, "Table_S4_threshold_sensitivity_sweeps.csv")
    with open(s4_path, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))[1:]
    taus = [r[0] for r in rows]
    accs = [r[1] for r in rows]
    escs = [r[6] for r in rows]
    assert taus == ["tau = 0.70", "tau = 0.80", "tau = 0.85", "tau = 0.90", "tau = 0.95"]
    assert accs == ["96.35%", "96.61%", "97.14%", "97.40%", "97.92%"]
    assert escs == ["0.5%", "1.6%", "2.6%", "3.4%", "9.1%"]
    print("  --> PASS: Table S4 monotonic escalation and accuracy verified.")

def test_s5_dataset_invariants():
    print("[TEST 4] Verifying Table S5 (Corpus Breakdown) Invariants...")
    s5_path = os.path.join(TABLES_DIR, "Table_S5_dataset_partitions_breakdown.csv")
    with open(s5_path, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))[1:]
    assert "1,726 (72.0%)" in rows[0][3] and "671 (28.0%)" in rows[0][4]  # Train N=2397
    assert "192 (71.9%)" in rows[1][3] and "75 (28.1%)" in rows[1][4]      # Holdout N=267
    assert "19 (16.2%)" in rows[2][3] and "98 (83.8%)" in rows[2][4]       # Challenge N=117
    assert "211 (54.9%)" in rows[3][3] and "173 (45.1%)" in rows[3][4]     # Dev N=384
    assert "1,918 (72.0%)" in rows[4][3] and "746 (28.0%)" in rows[4][4]   # Full N=2664
    print("  --> PASS: Table S5 class balance and sample sizes verified.")

def test_prompts_and_pii_rules():
    print("[TEST 5] Verifying Prompt configurations and PII Sanitizer...")
    for yml in ["gemini_3.5_flash_5shot_icl.yaml", "p_single_forensic_prompt.yaml", "tier2_council_3agent_prompts.yaml", "tier2_council_5agent_prompts.yaml"]:
        p = os.path.join(PROMPTS_DIR, yml)
        with open(p, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            assert data is not None, f"Failed to load {yml}"
    with open(os.path.join(PROMPTS_DIR, "pii_sanitizer_regex_rules.json"), "r", encoding="utf-8") as f:
        pii = json.load(f)
        assert len(pii["rules"]) == 5, "Expected 5 PII redaction rules"
    print("  --> PASS: All prompt files and PII regex rules parsed successfully.")

if __name__ == "__main__":
    test_tables_exist()
    test_s3_confusion_invariants()
    test_s4_threshold_invariants()
    test_s5_dataset_invariants()
    test_prompts_and_pii_rules()
    print("\n[ALL INVARIANT TESTS PASSED SUCCESSFULLY!]")
