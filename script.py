"""
BSM - Talcum LT FIVE9 TEST
Lead Prosper API Integration
Campaign ID: 33842 | Supplier ID: 109647
"""

import requests
import json
from datetime import datetime

# ─── Campaign Credentials (DO NOT CHANGE) ─────────────────────────────────────
LP_CAMPAIGN_ID = "33842"
LP_SUPPLIER_ID = "109647"
LP_KEY         = "vwnhkyekc1m2x"
API_URL        = "https://api.leadprosper.io/direct_post"


def submit_lead(lead_data: dict, test_mode: bool = False) -> dict:
    """
    Submit a single lead to Lead Prosper.

    Parameters
    ----------
    lead_data : dict   – All lead fields (see REQUIRED_FIELDS below).
    test_mode : bool   – If True, adds lp_action=test so the lead bypasses
                         filters / caps and is never counted.

    Returns
    -------
    dict with keys: status, code, message, id, lead_id
    """
    payload = {
        "lp_campaign_id": LP_CAMPAIGN_ID,
        "lp_supplier_id": LP_SUPPLIER_ID,
        "lp_key":         LP_KEY,
    }

    if test_mode:
        payload["lp_action"] = "test"

    payload.update(lead_data)

    headers = {"Content-Type": "application/json"}

    try:
        resp = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.Timeout:
        return {"status": "ERROR", "code": -1, "message": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"status": "ERROR", "code": -2, "message": str(e)}


def validate_lead(lead_data: dict) -> list[str]:
    """
    Validate required fields before submission.
    Returns a list of error messages (empty list = all good).
    """
    REQUIRED_FIELDS = [
        "Center_Code",
        "ip_adress",
        "first_name",
        "last_name",
        "number1",
        "email",
        "Diagnosis_Date",
        "verification_id",
        "Proof_of_Medication",
        "Photo_ID_URL",
        "Social_Security",
    ]

    errors = []
    for field in REQUIRED_FIELDS:
        if field not in lead_data or not str(lead_data[field]).strip():
            errors.append(f"Missing required field: {field}")

    # Basic phone check
    if "number1" in lead_data:
        phone = str(lead_data["number1"]).replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
        if not phone.isdigit() or len(phone) != 10:
            errors.append("number1 must be a 10-digit US phone number")

    # Basic email check
    if "email" in lead_data and "@" not in str(lead_data["email"]):
        errors.append("email must be a valid email address")

    # Social Security: last 4 digits only
    if "Social_Security" in lead_data:
        ssn = str(lead_data["Social_Security"]).strip()
        if not ssn.isdigit() or len(ssn) != 4:
            errors.append("Social_Security must be exactly 4 digits")

    # DOB format check
    if "date_of_birth" in lead_data:
        try:
            datetime.strptime(lead_data["date_of_birth"], "%m/%d/%Y")
        except ValueError:
            errors.append("date_of_birth must be in MM/DD/YYYY format")

    return errors


def print_result(result: dict):
    """Pretty-print the API response."""
    status = result.get("status", "UNKNOWN")
    icons = {"ACCEPTED": "✅", "DUPLICATED": "⚠️", "ERROR": "❌"}
    icon = icons.get(status, "❓")

    print(f"\n{icon} Status  : {status}")
    print(f"   Code    : {result.get('code', 'N/A')}")
    print(f"   Message : {result.get('message', '')}")
    print(f"   ID      : {result.get('id', 'N/A')}")
    print(f"   Lead ID : {result.get('lead_id', 'N/A')}\n")
