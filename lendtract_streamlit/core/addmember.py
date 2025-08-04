import os
from datetime import datetime
from openpyxl import Workbook
from core.utils import get_member_path

def add_member(name, loan_amount, interest_rate, loan_period, monthly_interest):
    if not name.strip() or loan_amount < 0 or interest_rate < 0 or loan_period < 1:
        return False  # Invalid inputs

    filename = get_member_path(name)
    if os.path.exists(filename):
        return False  # Member already exists

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Payments"

        # Header Row
        ws.append([
            "Name", "Loan Amount", "Interest Rate (%)", "Start Date",
            "Loan Period (Months)", "Monthly Interest",
            "Payment Date", "Amount Paid", "Notes"
        ])

        # Borrower Info
        ws.append([
            name, loan_amount, interest_rate,
            datetime.now().strftime("%Y-%m-%d"),
            loan_period, monthly_interest,
            "", "", ""
        ])

        wb.save(filename)
        return True
    except Exception as e:
        print(f"Error saving member data: {e}")
        return False