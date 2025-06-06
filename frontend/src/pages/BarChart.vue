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

const series = ref([])
const chartOptions = ref({
    chart: {
        type: 'bar',
        toolbar: { show: false },
    },
    colors: ['#10b981', '#ef4444'],
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

// Helper: convert month name to month index
const getMonthIndex = (monthStr) => {
    // Works with short month names like "Jan", "Feb", etc.
    return new Date(Date.parse(monthStr + " 1, 2000")).getMonth()
}

onMounted(async () => {
    try {
        const res = await axios.get(
            '/api/method/student_portal_access.studentAttendance.get_student_attendance_summary'
        )

        const data = res.data.message

        // Combine month, present, and absent into one array
        const combined = data.labels.map((label, index) => ({
            label,
            present: data.present[index],
            absent: data.absent[index],
        }))

        // Sort by month index dynamically
        combined.sort((a, b) => getMonthIndex(a.label) - getMonthIndex(b.label))

        // Extract sorted arrays
        const sortedLabels = combined.map(item => item.label)
        const sortedPresent = combined.map(item => item.present)
        const sortedAbsent = combined.map(item => item.absent)

        series.value = [
            { name: 'Present', data: sortedPresent },
            { name: 'Absent', data: sortedAbsent },
        ]
        chartOptions.value.xaxis.categories = sortedLabels
    } catch (error) {
        console.error('Failed to fetch attendance:', error)
    }
})
</script>



