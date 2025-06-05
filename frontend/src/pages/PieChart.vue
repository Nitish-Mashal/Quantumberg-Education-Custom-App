<template>
    <div class="p-4 bg-white shadow rounded">
        <apexchart type="pie" height="300" :options="chartOptions" :series="series" />
        <div class="mt-4 text-center">
            <button class="bg-pink-600 text-white px-6 py-2 rounded shadow">My Courses</button>
        </div>
    </div>
</template>

<script setup>
const series = [450, 470, 584, 872, 536]

const chartOptions = {
    labels: ['Math', 'Science', 'English', 'History', 'CS'],
    colors: ['#a855f7', '#ec4899', '#f59e0b', '#10b981', '#3b82f6'],
    legend: {
        position: 'bottom',
    },
}
</script>
