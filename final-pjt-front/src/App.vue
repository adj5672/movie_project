<template>
  <div id="app">
    <div id="nav" class="d-flex justify-content-between align-items-center px-5 mx-5">
      <div class="d-flex align-items-center">
        <img src="@/assets/logo.png" alt="logo" style="height: 80px;" class="me-4">
        <router-link class="mx-3" :to="{ name: 'AllMovies' }">전체영화</router-link>
        <router-link class="mx-3" :to="{ name: 'RecommandMovies' }">추천영화</router-link>
      </div>
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
  methods: {
    currentTime: function () {
      this.$store.state.Year = this.$moment().format('YYYY')
      this.$store.state.Month = this.$moment().format('MM')
      this.$store.state.Day = this.$moment().format('DD')
      this.$store.state.Hour = this.$moment().format('HH')
      this.$store.state.Minute = this.$moment().format('mm')
      this.$store.state.Second = this.$moment().format('ss')
    }
  },
  created: function () {
    // 실시간 시간 정보 받아오기
    setInterval(this.currentTime, 1000)
    // 전체 영화 정보 받아오기
    this.$store.dispatch('getAllMovies')
    // 로그인 여부 확인
    const token = localStorage.getItem('jwt')
    if (token) {
      this.$store.dispatch('logIn', token)
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 600px;
}

#app input {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

#nav {
  font-family: 'Jua', sans-serif;
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration-line: none;
  font-size: 1.5rem;
}

#nav a.router-link-exact-active {
  color: red;
}
</style>
