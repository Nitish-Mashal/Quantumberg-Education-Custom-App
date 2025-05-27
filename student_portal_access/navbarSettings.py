import frappe

def setup_help_dropdown():
    try:
        navbar = frappe.get_doc("Navbar Settings")

        # Labels to hide
        to_hide = [
            "Documentation",
            "User Forum",
            "Frappe School",
            "Report an Issue",
            "About",
            "Frappe Support"
        ]

        # Hide specified items
        for item in navbar.help_dropdown:
            if item.item_label in to_hide:
                item.hidden = 1

        # Add custom documentation link if not already present
        if not any(item.item_label == "Education Documentation" for item in navbar.help_dropdown):
            navbar.append("help_dropdown", {
                "item_label": "Education Documentation",
                "item_type": "Route",
                "route": "https://quantumberg.github.io/qdynamics-education-mkdoc-documentation/",
                "hidden": 0
            })

        navbar.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint("Custom Help Dropdown applied successfully.")
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Navbar Setup Error")

def revert_help_dropdown():
    try:
        navbar = frappe.get_doc("Navbar Settings")

        # Unhide original items
        to_unhide = [
            "Documentation",
            "User Forum",
            "Frappe School",
            "Report an Issue",
            "About",
            "Frappe Support"
        ]

        for item in navbar.help_dropdown:
            if item.item_label in to_unhide:
                item.hidden = 0

        # Remove custom documentation item
        navbar.help_dropdown = [
            item for item in navbar.help_dropdown
            if item.item_label != "Education Documentation"
        ]

        navbar.save(ignore_permissions=True)
        frappe.db.commit()
        frappe.msgprint("Help Dropdown reverted to default.")
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Navbar Revert Error")
