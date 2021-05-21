<template>
  <w-app>
    <div id="app">
      <div id="nav">
        <router-link :to="{ name: 'AllMovies' }">전체영화</router-link> |
        <router-link :to="{ name: 'RecommandMovies' }">추천영화</router-link> | 
        <router-link :to="{ name: 'Signup' }" v-if="!this.$store.state.isLogin">회원가입</router-link>
        <SideBar/>
      </div>
      <router-view/>
      <MovieDetail/>
    </div>
  </w-app>
</template>

<script>
import SideBar from '@/views/Accounts/SideBar'
import MovieDetail from '@/components/Movies/MovieDetail'

export default {
  name: 'App',
  components: {
    SideBar,
    MovieDetail
  },
  created: function () {
    this.$store.dispatch('getAllMovies')
    const token = localStorage.getItem('jwt')
    if (token) {
      this.$store.state.isLogin = true
      this.$store.state.config = {
        Authorization: `JWT ${token}`
      }
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
