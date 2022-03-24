import { createApp } from 'vue'
import App from './App.vue'
import store from './store/index'
import router from './router/routes'

createApp(App)
    .use(router)
    .use(store)
    .mount('#app')
