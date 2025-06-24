import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/', redirect: '/Home' },
  {
    path: '/Home',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/student-portal-dashboard/'),
  routes,
})

export default router