<template>
  <div id="app">
    <div id="nav" class="border border-dark">
      <router-link :to="{ name: 'AllMovies' }">전체영화</router-link> |
      <router-link :to="{ name: 'RecommandMovies' }">추천영화</router-link> | 
      <router-link :to="{ name: 'Signup' }">회원가입</router-link>
      <SideBar/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import SideBar from '@/views/SideBar'

export default {
  name: 'App',
  components: {
    SideBar,
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
