import Vue from 'vue'
import VueRouter from 'vue-router'
import AllMovies from '@/views/AllMovies'
import RecommandMovies from '@/views/RecommandMovies'
import Signup from '@/views/Signup'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'AllMovies',
    component: AllMovies
  },
  {
    path: '/RecommandMovies',
    name: 'RecommandMovies',
    component: RecommandMovies
  },
  {
    path: '/Signup',
    name: 'Signup',
    component: Signup
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
