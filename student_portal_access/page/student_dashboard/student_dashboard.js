frappe.pages['student-dashboard'].on_page_load = function (wrapper) {
    frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Student Dashboard',
        single_column: true
    });

    // Hide side navbar
    $('.layout-side-section').hide();

    const links = [
        { label: 'Schedule', route: '/student-portal/schedule' },
        { label: 'Grades', route: '/student-portal/grades' },
        { label: 'Fees', route: '/student-portal/fees' },
        { label: 'Attendance', route: '/student-portal/attendance' }
    ];

    const html = links.map(link => `
        <div style="margin: 1rem 0;">
            <a href="${link.route}" class="btn btn-primary" style="width: 200px;">${link.label}</a>
        </div>
    `).join('');

    $(wrapper).find('.layout-main-section').html(`
        <div style="padding: 2rem;">
            <h3>Welcome to Student Dashboard</h3>
            ${html}
        </div>
    `);
};
