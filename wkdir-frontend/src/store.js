import Vue from 'vue'
import Vuex from 'vuex'
// import axios from './axios-auth'
// import globalAxios from 'axios'

// import router from './router'

Vue.use(Vuex)

export const store =  new Vuex.Store({
  state: {
    showbanner: false,
  },
  mutations: {
    togglebanner(state) {
      state.showbanner = true
    },
  },
  actions: {
    togglebanner ({commit}) {
      commit('togglebanner')
    },
  }
})