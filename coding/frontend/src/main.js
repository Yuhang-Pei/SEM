import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App);

axios.defaults.baseURL = 'http://localhost:5000';
app.config.globalProperties.$http = axios;

app.use(router).mount('#app');