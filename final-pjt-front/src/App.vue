<template>
  <div id="app">
    <div id="nav" class="d-flex justify-content-between align-items-center bg-white"  style="padding-left: 15%; padding-right: 15%;">
      <div class="d-flex align-items-center">
        <img src="@/assets/logo.png" alt="logo" style="height: 130px;" class="me-4">
        <router-link class="mx-3" :to="{ name: 'AllMovies' }">전체영화</router-link>
        <router-link class="mx-3" :to="{ name: 'RecommandMovies' }">추천영화</router-link>
      </div>
      <SideBar/>
    </div>
    <router-view/>
    <MovieDetail @updateMyMovies="updateMyMovies"/>
    <ReviewDetail/>
    <CommentDetail/>
    <div id="footer" class="border-top" style="margin-left: 15%; margin-right: 15%;">
      <h6 class="text-center py-3">Copyright ⓒ An 2021. All Rights Reserved</h6>
    </div>
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
    },
    updateMyMovies: function () {
      this.$store.dispatch('getMyMovies')
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
  },
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
  min-width: 1000px;
  transition-duration: 2s;
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
  font-size: 2.2rem;
}

#nav a.router-link-exact-active {
  color: red;
}

#footer h6 {
  font-family: 'Jua', sans-serif;;
}
</style>
