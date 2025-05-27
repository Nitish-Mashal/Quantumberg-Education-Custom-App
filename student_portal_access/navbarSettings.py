def patch_help_dropdown(bootinfo):
    labels_to_hide = {
        "Documentation",
        "User Forum",
        "Frappe School",
        "Report an Issue",
        "About",
        "Frappe Support"
    }

    if "help_dropdown" in bootinfo:
        for item in bootinfo["help_dropdown"]:
            if item.get("item_label") in labels_to_hide:
                item["hidden"] = 1

    bootinfo.setdefault("help_dropdown", []).append({
        "item_label": "Education Documentation",
        "item_type": "route",
        "route": "https://quantumberg.github.io/qdynamics-education-mkdoc-documentation/",
        "hidden": 0
    })
