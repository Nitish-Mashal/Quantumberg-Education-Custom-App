<template>
  <div v-if="!authChecked" class="p-4">Checking authorization...</div>

  <div v-else class="flex h-screen">
    <Sidebar :isOpen="isSidebarOpen" />
    <div class="flex-1 flex flex-col">
      <Topbar @toggle-sidebar="toggleSidebar" />
      <div class="p-4">
        <FeatureCards />
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <BarChart />
          <PieChart />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Sidebar from './Sidebar.vue'
import Topbar from './Topbar.vue'
import FeatureCards from './FeatureCards.vue'
import BarChart from './BarChart.vue'
import PieChart from './PieChart.vue'

const isSidebarOpen = ref(false)
const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const router = useRouter()
const authChecked = ref(false) // NEW

const checkAuth = async () => {
  try {
    const res = await fetch('/api/method/student_portal_access.api.auth.get_logged_in_user', {
      credentials: 'include'
    })

    if (!res.ok) throw new Error('Unauthorized')

    const data = await res.json()
    console.log('User:', data.message)
    authChecked.value = true

  } catch (err) {
    console.warn('Access denied, redirecting to login...')
    router.push('/login#login')
  }
}

onMounted(() => {
  checkAuth()
})
</script>
