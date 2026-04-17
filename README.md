# BSM – Talcum LT FIVE9 TEST
## Lead Prosper API Integration

Campaign ID: **33842** | Supplier ID: **109647**  
Endpoint: `POST https://api.leadprosper.io/direct_post`

---

## Files

| File | Purpose |
|------|---------|
| `lead_submit.py` | Python module – submit leads, validate fields |
| `test_lead.py` | Run automated tests (TEST mode + validation checks) |
| `lead_form.html` | Open in browser – interactive HTML form for manual testing |

---

## Quick Start

### 1. Install dependency
```bash
pip install requests
```

### 2. Run the test script
```bash
python test_lead.py
```
This runs 4 tests:
- **Test 1** – Validates all required fields are present
- **Test 2** – Submits a full lead in TEST mode (`lp_action=test`)
- **Test 3** – Submits a minimal (required-only) lead in TEST mode
- **Test 4** – Intentionally triggers validation errors

### 3. Use the HTML form
Open `lead_form.html` in any browser.  
- **TEST mode** – adds `lp_action=test` (bypasses filters/caps, not counted)
- **LIVE mode** – submits a real lead

---

## Required Fields

| Field | Description |
|-------|-------------|
| `lp_campaign_id` | Auto-set to `33842` |
| `lp_supplier_id` | Auto-set to `109647` |
| `lp_key` | Auto-set to `vwnhkyekc1m2x` |
| `Center_Code` | Your publisher ID |
| `ip_adress` | Lead's IP address |
| `first_name` | Lead first name |
| `last_name` | Lead last name |
| `number1` | US phone, e.g. `(650) 327-1100` |
| `email` | Valid email address |
| `Diagnosis_Date` | Date of diagnosis |
| `verification_id` | TrustedForm cert ID/URL |
| `Proof_of_Medication` | URL to proof of medication doc |
| `Photo_ID_URL` | URL to photo ID doc |
| `Social_Security` | Last **4 digits** only |

---

## API Responses

| Status | Code | Meaning |
|--------|------|---------|
| `ACCEPTED` | 0 | Lead accepted ✅ |
| `DUPLICATED` | 1008 | Duplicate lead ⚠️ |
| `ERROR` | 1013 | Lead rejected ❌ |

---

## Testing Mode

Add `lp_action=test` to any request to force a test that:
- Skips all configured filters
- Skips cap limits
- Is **not** counted as a real lead

---

## Support
Questions? Email: michael.b@thelegalleads.com

> ⚠️ Fields are **case sensitive** — `first_name` ≠ `First_Name`
