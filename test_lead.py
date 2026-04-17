"""
BSM - Talcum LT FIVE9 TEST
Test Script  –  run with:  python test_lead.py
"""

from lead_submit import submit_lead, validate_lead, print_result

# ─── Sample Test Lead (all fields) ────────────────────────────────────────────
# lp_action is set to "test" inside submit_lead() when test_mode=True
# This means it bypasses filters / caps and is NOT counted as a real lead.

SAMPLE_LEAD = {
    # ── Required ──────────────────────────────────────────────────────────────
    "Center_Code":          "YOUR_PUBLISHER_ID",      # ← replace with your ID
    "ip_adress":            "192.168.1.100",
    "first_name":           "Jane",
    "last_name":            "Doe",
    "number1":              "(555) 123-4567",         # US format
    "email":                "janedoe@example.com",
    "Diagnosis_Date":       "2022-03-15",
    "verification_id":      "TRUSTEDFORM_CERT_ID",    # ← TrustedForm cert URL/ID
    "Proof_of_Medication":  "https://example.com/proof_of_medication.pdf",
    "Photo_ID_URL":         "https://example.com/photo_id.jpg",
    "Social_Security":      "1234",                   # Last 4 digits only

    # ── Optional ──────────────────────────────────────────────────────────────
    "lp_subid1":                "sub1_value",
    "lp_subid2":                "sub2_value",
    "Agent_Name":               "Agent Smith",
    "data_source":              "web_form",
    "other_cancer_type":        "Ovarian",
    "verification_id_2":        "JORNAYA_LEAD_ID",    # Jornaya ID
    "street":                   "123 Main St",
    "city":                     "Springfield",
    "state":                    "IL",
    "zip":                      "62701",
    "date_of_birth":            "04/15/1965",         # MM/DD/YYYY
    "notes":                    "Called back twice",
    "external_id":              "EXT-98765",
    "currently_working_with_attorney": "No",
    "medication":               "Aspirin",
    "who_is_doctor":            "Dr. Smith",
    "inquiry_date":             "04/17/2026",
    "alt_phone":                "(555) 987-6543",
    "Proof_Of_Cancer":          "https://example.com/cancer_proof.pdf",
    "plaid_ID":                 "",
    "Where_Diagnosed":          "Springfield General Hospital",
    "Diagnosed_Address":        "100 Hospital Blvd, Springfield, IL",
    "Diagnosed_Phone":          "(555) 200-0000",
    "Diagnosing_Doctor":        "Dr. Jones",
    "Where_Treated":            "Springfield Cancer Center",
    "Treated_Address":          "200 Cancer Ln, Springfield, IL",
    "Treated_Phone":            "(555) 300-0000",
    "Treated_Doctor":           "Dr. Brown",
}


def run_tests():
    print("=" * 60)
    print("  BSM - Talcum LT FIVE9 TEST  |  Lead Prosper API Tests")
    print("=" * 60)

    # ── Test 1: Validation ────────────────────────────────────────────────────
    print("\n[TEST 1] Validating required fields...")
    errors = validate_lead(SAMPLE_LEAD)
    if errors:
        print("  ❌ Validation FAILED:")
        for e in errors:
            print(f"     • {e}")
    else:
        print("  ✅ All required fields pass validation")

    # ── Test 2: Live test submission (lp_action=test) ─────────────────────────
    print("\n[TEST 2] Submitting TEST lead (lp_action=test)...")
    print("  ℹ️  Bypasses filters/caps — not counted as a real lead")
    result = submit_lead(SAMPLE_LEAD, test_mode=True)
    print_result(result)

    # ── Test 3: Minimal required-fields-only submission ───────────────────────
    print("[TEST 3] Submitting minimal (required fields only) TEST lead...")
    minimal_lead = {
        "Center_Code":         "YOUR_PUBLISHER_ID",
        "ip_adress":           "10.0.0.1",
        "first_name":          "John",
        "last_name":           "Smith",
        "number1":             "(444) 555-6666",
        "email":               "jsmith@example.com",
        "Diagnosis_Date":      "2021-06-01",
        "verification_id":     "TRUSTEDFORM_CERT_ID",
        "Proof_of_Medication": "https://example.com/meds.pdf",
        "Photo_ID_URL":        "https://example.com/id.jpg",
        "Social_Security":     "5678",
    }
    result2 = submit_lead(minimal_lead, test_mode=True)
    print_result(result2)

    # ── Test 4: Validation failure demo ───────────────────────────────────────
    print("[TEST 4] Intentional validation failure (missing fields)...")
    bad_lead = {"first_name": "NoEmail"}
    errors2 = validate_lead(bad_lead)
    if errors2:
        print("  ✅ Correctly caught errors:")
        for e in errors2:
            print(f"     • {e}")
    print()


if __name__ == "__main__":
    run_tests()
