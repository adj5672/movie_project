import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Carousel3d from 'vue-carousel-3d'
import 'element-ui/lib/theme-chalk/index.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Carousel3d)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
