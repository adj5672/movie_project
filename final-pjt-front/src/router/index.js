import Vue from 'vue'
import VueRouter from 'vue-router'
import AllMovies from '@/views/Movies/AllMovies'
import RecommandMovies from '@/views/Movies/RecommandMovies'
import MyMovies from '@/views/Movies/MyMovies'
import MyReviews from '@/views/Community/MyReviews'
import Signup from '@/views/Accounts/Signup'

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
  {
    path: '/MyMovies',
    name: 'MyMovies',
    component: MyMovies
  },
  {
    path: '/MyReviews',
    name: 'MyReviews',
    component: MyReviews
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
