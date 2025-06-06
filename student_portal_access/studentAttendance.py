import frappe
from frappe.utils import getdate
from frappe import _
from frappe import whitelist
from collections import defaultdict

@frappe.whitelist()
def get_student_attendance_summary():
    student_id = frappe.get_value("Student", {"user": frappe.session.user})
    if not student_id:
        frappe.throw(_("Student not found for this user."))

    attendance_data = frappe.get_all(
        "Student Attendance",
        filters={"student": student_id, "docstatus": 1},
        fields=["status", "date"]  # ✅ Use correct field
    )

    summary = defaultdict(lambda: {"Present": 0, "Absent": 0})

    for record in attendance_data:
        month = getdate(record.date).strftime("%b")  # ✅ Corrected this line
        summary[month][record.status] += 1

    labels = []
    present_data = []
    absent_data = []
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    for month in month_order:
        if month in summary:
            labels.append(month)
            present_data.append(summary[month]["Present"])
            absent_data.append(summary[month]["Absent"])

    return {
        "labels": labels,
        "present": present_data,
        "absent": absent_data
    }
