import Vue from 'vue'

import App from './App.vue'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { store } from './store'
 
Vue.use(VueAxios, axios)

Vue.prototype.bus = new Vue()

Vue.prototype.ss = false

import M from 'materialize-css'

Vue.prototype.toast = (msg, lvl) => {
  if(lvl == 'ok'){
    M.toast({html: msg, classes: 'rounded green'});
  }else{
    M.toast({html: msg, classes: 'rounded'});
  }
}


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
