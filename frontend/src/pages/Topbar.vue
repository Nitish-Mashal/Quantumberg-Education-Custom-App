<template>
    <div class="flex justify-between items-center p-4 shadow relative">
        <!-- Sidebar Toggle -->
        <button class="text-2xl" @click="$emit('toggle-sidebar')">&#9776;</button>

        <!-- Right side -->
        <div class="flex items-center gap-4 relative">
            <button class="bg-pink-600 text-white px-4 py-2 rounded shadow flex items-center gap-2">
                + Explore More
            </button>

            <!-- Notification Bell -->
            <div class="relative cursor-pointer" @click="toggleNotifications">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-pink-600" viewBox="0 0 24 24"
                    fill="currentColor">
                    <path
                        d="M5.85 3.5a.75.75 0 0 0-1.117-1 9.719 9.719 0 0 0-2.348 4.876.75.75 0 0 0 1.479.248A8.219 8.219 0 0 1 5.85 3.5ZM19.267 2.5a.75.75 0 1 0-1.118 1 8.22 8.22 0 0 1 1.987 4.124.75.75 0 0 0 1.48-.248A9.72 9.72 0 0 0 19.266 2.5Z" />
                    <path fill-rule="evenodd"
                        d="M12 2.25A6.75 6.75 0 0 0 5.25 9v.75a8.217 8.217 0 0 1-2.119 5.52.75.75 0 0 0 .298 1.206c1.544.57 3.16.99 4.831 1.243a3.75 3.75 0 1 0 7.48 0 24.583 24.583 0 0 0 4.83-1.244.75.75 0 0 0 .298-1.205 8.217 8.217 0 0 1-2.118-5.52V9A6.75 6.75 0 0 0 12 2.25ZM9.75 18c0-.034 0-.067.002-.1a25.05 25.05 0 0 0 4.496 0l.002.1a2.25 2.25 0 1 1-4.5 0Z"
                        clip-rule="evenodd" />
                </svg>
                <span v-if="hasNew" class="absolute top-0 right-0 h-2 w-2 bg-red-600 rounded-full"></span>
            </div>

            <!-- Dropdown -->
            <div v-if="showNotifications" class="absolute right-0 top-12 w-80 bg-white shadow rounded z-50 p-2">
                <p v-if="notifications.length === 0" class="text-sm text-gray-500">No notifications</p>
                <ul v-else>
                    <li v-for="(note, index) in notifications" :key="index" class="text-sm py-2 border-b">
                        <div class="flex justify-between items-start gap-2">
                            <div>
                                <span class="font-semibold text-xs text-pink-600">[{{ note.type }}]</span>
                                {{ note.message }}
                                <div v-if="note.docType && note.docName" class="text-xs text-blue-600 underline">
                                    <a :href="`/app/${note.docType}/${note.docName}`" target="_blank">View {{
                                        note.docType }}</a>
                                </div>
                            </div>
                            <span class="text-xs text-gray-400 whitespace-nowrap">{{ note.time }}</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const notifications = ref([]);
const showNotifications = ref(false);
const hasNew = ref(false);
const currentUser = ref('');

function toggleNotifications() {
    showNotifications.value = !showNotifications.value;
    hasNew.value = false;
}

onMounted(async () => {
    console.log('🔄 onMounted triggered');

    // 1. Get logged-in user
    const userRes = await fetch('/api/method/student_portal_access.api.auth.get_logged_in_user', {
        credentials: 'include'
    });

    const userData = await userRes.json();
    console.log('Logged-in user response:', userData);

    currentUser.value = userData.message.email;
    console.log('Current user email:', currentUser.value);

    // 2. Fetch existing notifications
    const res = await fetch('/api/method/student_portal_access.api.notifications.get_all_user_notifications', {
        credentials: 'include'
    });

    const data = await res.json();
    console.log('Fetched notifications:', data);

    notifications.value = (data.message || []).map(note => ({
        message: note.message,
        time: note.time,
        type: note.type || 'Info',
        docType: note.document_type,
        docName: note.document_name
    }));

    // 3. Listen for realtime notifications scoped to the user
    if (window.frappe?.realtime && currentUser.value) {
        const channel = `notification_${currentUser.value}`;
        console.log(`Subscribing to real-time channel: ${channel}`);

        window.frappe.realtime.on(channel, (data) => {
            console.log('📡 Real-time notification received:', data);
            notifications.value.unshift({
                message: data.message,
                time: new Date().toLocaleString(),
                type: data.type || 'Info',
                docType: data.document_type,
                docName: data.document_name
            });
            hasNew.value = true;
        });
    } else {
        console.warn('Real-time not available or user email missing');
    }
});
</script>