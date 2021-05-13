import Vue from 'vue'
import App from './App.vue'
import store from './store'
import UUID from 'vue-uuid'

Vue.use(UUID) // 등록
Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
