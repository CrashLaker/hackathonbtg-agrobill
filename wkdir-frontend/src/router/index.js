import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/agrobill',
    name: 'agrobill',
    component: () => import('../views/Agrobill.vue')
  },
  {
    path: '/financing/historico',
    name: 'financinghistorico',
    component: () => import('../views/FinancingHistorico.vue')
  },
  {
    path: '/financing/confirm',
    name: 'financingconfirm',
    component: () => import('../views/FinancingConfirm.vue')
  },
  {
    path: '/financing/assessoria',
    name: 'financingassessoria',
    component: () => import('../views/FinancingAssessoria.vue')
  },
  {
    path: '/financing/lead',
    name: 'financinglead',
    component: () => import('../views/FinancingLead.vue')
  },
  {
    path: '/financing/:url(.*?)',
    name: 'financing',
    component: () => import('../views/Financing.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
