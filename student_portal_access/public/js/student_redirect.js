// (function () {
//     frappe.after_ajax(() => {
//         const user = frappe.session.user;
//         const roles = frappe.boot.user.roles;

//         // Only redirect Student users from default welcome-workspace
//         if (
//             roles.includes("Student") &&
//             frappe.get_route_str() === "welcome-workspace"
//         ) {
//             frappe.set_route("student-portal/schedule"); // your custom workspace route
//         }
//     });
// })();

// Run only if user is on the home page
// console.log("New Student code for path redirection to stydent portal")
// if (frappe.boot && window.location.pathname === "/app") {
//     const userRoles = frappe.boot.user.roles || [];

//     if (userRoles.includes("Student")) {
//         window.location.href = "/student-portal/schedule";
//     }
// }
