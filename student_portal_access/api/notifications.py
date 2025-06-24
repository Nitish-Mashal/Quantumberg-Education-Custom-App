import frappe
from frappe.utils import format_datetime, now_datetime, get_datetime

@frappe.whitelist()
def get_all_user_notifications():
    """Fetch last 20 notifications only for the logged-in user."""
    user = frappe.session.user
    logs = frappe.get_all(
        "Notification Log",
        filters={"for_user": user},
        fields=["subject", "email_content", "creation", "type", "document_type", "document_name"],
        order_by="creation desc",
        limit_page_length=20
    )

    return [
        {
            "message": log.subject or log.email_content,
            "time": format_datetime(log.creation, "medium"),
            "type": log.type,
            "document_type": log.document_type,
            "document_name": log.document_name
        } for log in logs
    ]

def push_realtime_notification(doc, method=None):
    if doc.for_user:
        frappe.publish_realtime(
            event=f"notification_{doc.for_user}",  # user-specific channel
            message={
                "message": doc.subject or doc.email_content,
                "type": doc.type,
                "document_type": doc.document_type,
                "document_name": doc.document_name
            },
            user=doc.for_user
        )

@frappe.whitelist()
def send_test_notification():
    user = frappe.session.user

    doc = frappe.new_doc("Notification Log")
    doc.for_user = user
    doc.type = "Alert"
    doc.subject = "Hello from Frappe!"
    doc.email_content = "This is a test push notification."
    doc.save(ignore_permissions=True)

    return {"status": "Notification Created"}


def fix_student_notification_recipient(doc, method=None):
    """Fix Notification Log to set correct for_user if missing"""
    if not doc.user:
        return  # skip if user not linked to student

    recent_logs = frappe.get_all(
        "Notification Log",
        filters={
            "document_type": "Student",
            "document_name": doc.name,
            "for_user": None,  # This is the correct way to filter IS NULL
            "creation": [">", frappe.utils.now_datetime().replace(minute=0, second=0)]
        },
        order_by="creation desc",
        limit_page_length=5
    )

    for log in recent_logs:
        log_doc = frappe.get_doc("Notification Log", log.name)
        log_doc.for_user = doc.user
        log_doc.save(ignore_permissions=True)
