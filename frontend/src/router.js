import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/'),
  routes,
})

export default router

// import { createRouter, createWebHistory } from 'vue-router'
// import axios from 'axios'

// const routes = [
//   {
//     path: '/',
//     name: 'Home',
//     component: () => import('@/pages/Home.vue'),
//   }
// ]

// const router = createRouter({
//   history: createWebHistory('/'),
//   routes,
// })

// // Global guard: Check Frappe session + student role
// router.beforeEach(async (to, from, next) => {
//   const sid = document.cookie.includes('sid=')

//   if (!sid) {
//     // Not logged in via Frappe
//     alert('You must log in via the Frappe system.')
//     return
//   }

//   try {
//     // Get logged-in user
//     const userRes = await axios.get('/api/method/frappe.auth.get_logged_user')
//     const user = userRes.data.message

//     // Get roles of the user
//     const detailRes = await axios.get(`/api/resource/User/${user}`)
//     const roles = detailRes.data.data.roles.map(r => r.role)

//     if (roles.includes('Student')) {
//       next() // allow access to home page
//     } else {
//       // Not a student
//       alert('Access denied: Only students can view this page.')

//     }
//   } catch (error) {
//     console.error('Auth error:', error)
//     alert('Something went wrong. Please try again later.')
//     return
//   }
// })

// export default router

