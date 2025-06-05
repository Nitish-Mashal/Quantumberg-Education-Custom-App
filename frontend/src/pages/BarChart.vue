<template>
    <div class="p-4 bg-white shadow rounded">
        <h2 class="text-lg font-semibold mb-2">Attendance Summary</h2>

        <apexchart v-if="series.length" type="bar" height="300" :options="chartOptions" :series="series" />

        <div v-else class="text-gray-500">Loading attendance data...</div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// Chart series and options
const series = ref([])
const chartOptions = ref({
    chart: {
        type: 'bar',
        toolbar: { show: false },
    },
    colors: ['#10b981', '#ef4444'], // green = present, red = absent
    xaxis: {
        categories: [],
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
        },
    },
    dataLabels: {
        enabled: false,
    },
    legend: {
        position: 'top',
    },
})

// On component mount, fetch attendance
onMounted(async () => {
    try {
        const res = await axios.get(
            '/api/method/student_portal_access.studentAttendance.get_student_attendance_summary'
        )

        const data = res.data.message
        series.value = [
            { name: 'Present', data: data.present },
            { name: 'Absent', data: data.absent },
        ]
        chartOptions.value.xaxis.categories = data.labels
    } catch (error) {
        console.error('Failed to fetch attendance:', error)
    }
})
</script>

<style scoped>
/* Optional: add some styling if needed */
</style>
  
