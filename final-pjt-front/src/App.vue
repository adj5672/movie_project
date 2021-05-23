<template>
  <div id="app">
    <div id="nav" class="d-flex justify-content-center align-items-center">
      <router-link class="mx-3" :to="{ name: 'AllMovies' }">전체영화</router-link>
      <router-link class="mx-3" :to="{ name: 'RecommandMovies' }">추천영화</router-link>
      <router-link class="mx-3" :to="{ name: 'Signup' }" v-if="!this.$store.state.isLogin">회원가입</router-link>
      <SideBar/>
    </div>
    <router-view/>
    <MovieDetail/>
    <ReviewDetail/>
    <CommentDetail/>
  </div>
</template>

<script>
import SideBar from '@/views/Accounts/SideBar'
import MovieDetail from '@/components/Movies/MovieDetail'
import ReviewDetail from '@/components/Community/Reviews/ReviewDetail'
import CommentDetail from '@/components/Community/Comments/CommentDetail'

export default {
  name: 'App',
  components: {
    SideBar,
    MovieDetail,
    ReviewDetail,
    CommentDetail,
  },
  created: function () {
    this.$store.dispatch('getAllMovies')
    const token = localStorage.getItem('jwt')
    if (token) {
      this.$store.dispatch('logIn', token)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
