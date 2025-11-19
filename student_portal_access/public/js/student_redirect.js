frappe.after_ajax(() => {
    const currentPath = window.location.pathname;
    const roles = frappe.boot?.user?.roles || [];

    // Redirect Student users to the Vue frontend home page
    if (roles.includes("Student") && currentPath === "/app/welcome-workspace" || currentPath === "/app/overview") {
        window.location.href = "/student-portal/schedule";
    }
});