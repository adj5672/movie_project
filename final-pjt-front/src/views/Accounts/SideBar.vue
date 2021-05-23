<template>
  <div>
    <el-button type="text" @click="drawer = true">
      <img src="@/assets/hamburger.png" alt="" style="height: 30px;">
    </el-button>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-if="!$store.state.isLogin">
      <div class="d-flex flex-column justify-content-between" style="height: 100%;">
        <div class="container">
          <h2 class="my-3">로그인</h2>
          <Login @close-drawer="drawer = false"/>
          <el-button @click="$router.push('Signup'); drawer=false">회원가입</el-button>
        </div>
        <Moment/>
      </div>
    </el-drawer>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-else>
      <div class="d-flex flex-column justify-content-between" style="height: 100%;">
        <div>
          <div class="my-3">
            <h1>Hello, {{ $store.state.username }}</h1>
            <img src="@/assets/profile_image.png" alt="profile" style="width: 70%;">
          </div>
          <div class="d-flex flex-column align-items-center">
            <el-button @click="myMovies" type="primary" style="width: 80%;">나만의 영화들</el-button>
            <br>
            <el-button @click="myReviews" type="success" style="width: 80%;">나의 리뷰들</el-button>
            <br>
            <el-button @click="logout" type="danger" style="width: 80%;">로그아웃</el-button>
          </div>
        </div>
        <Moment/>
      </div>
    </el-drawer>

  </div>
</template>

<script>
import Login from '@/components/Accounts/Login'
import Moment from '@/components/Moment'

export default {
  name: 'SideBar',
  data: function () {
    return {
      drawer: false,
    }
  },
  components: {
    Login,
    Moment,
  },
  methods: {
    logout: function () {
      this.drawer = false
      localStorage.removeItem('jwt')
      this.$store.dispatch('logOut')
    },
    myMovies: function () {
      this.drawer = false
      this.$store.dispatch('getMyMovies')
      this.$router.push({ name: 'MyMovies' })
    },
    myReviews: function () {
      this.drawer = false
      this.$store.dispatch('getMyReviews')
      this.$router.push({ name: 'MyReviews' })
    }
  },
}
</script>

<style>

</style>