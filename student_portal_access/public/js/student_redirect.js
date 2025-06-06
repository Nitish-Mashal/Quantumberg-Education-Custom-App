frappe.after_ajax(() => {
    const currentPath = window.location.pathname;
    const roles = frappe.boot?.user?.roles || [];

    if (roles.includes("Student") && currentPath === "/app/welcome-workspace") {
        window.location.href = "/student-portal/schedule";
    }
});