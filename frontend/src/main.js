import './index.css'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import VueApexCharts from 'vue3-apexcharts'

import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

let app = createApp(App)

setConfig('resourceFetcher', frappeRequest)

app.use(router)
app.use(resourcesPlugin)
app.use(VueApexCharts)
app.component('apexchart', VueApexCharts)

app.component('Button', Button)
app.mount('#app')
