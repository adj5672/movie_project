<template>
  <div id="Sidebar">
    <el-button type="text" @click="drawer = true">
      <img src="@/assets/hamburger.png" alt="" style="height: 30px;">
    </el-button>

    <el-drawer
      title=""
      :visible.sync="drawer"
      :with-header="false"
      size="300"
      v-if="!$store.state.isLogin">
      <div class="d-flex flex-column justify-content-between my-3" style="height: 100%; min-width: 300px;">
        <div class="container">
          <h2 class="my-3 fw-bold">로그인</h2>
          <Login @close-drawer="drawer = false"/>
          <el-button @click="$router.push('Signup'); drawer=false" style="font-weight: bold; font-size: 1.1rem; width: 197px;"><i class="el-icon-user-solid"></i> 회원가입</el-button>
        </div>
        <div class="pb-3">
          <Moment/>
        </div>
      </div>
    </el-drawer>

    <el-drawer
      title=""
      :visible.sync="drawer"
      :with-header="false"
      size="300"
      v-else>
      <div class="d-flex flex-column justify-content-between" style="height: 100%; min-width: 300px;">
        <div>
          <div class="my-3">
            <img src="@/assets/profile_image.png" alt="profile" style="width: 150px;">
            <h1 class="fw-bold my-3"><i class="el-icon-user-solid"></i> {{ $store.state.username }}</h1>
          </div>
          <div class="d-flex flex-column align-items-center mt-4">
            <div class="d-flex flex-column w-75">
              <el-button @click="myMovies" type="primary" style="font-size: 1.1rem;"><i class="el-icon-video-camera-solid"></i> 나만의 영화</el-button>
              <br>
              <el-button @click="myReviews" type="success" style="font-size: 1.1rem;"><i class="el-icon-document"></i> 나의 리뷰</el-button>
              <br>
              <el-button @click="myComments" type="warning" style="font-size: 1.1rem;"><i class="el-icon-chat-dot-round"></i> 나의 댓글</el-button>
              <br>
              <el-button @click="logout" type="danger" style="font-size: 1.1rem;"><i class="el-icon-switch-button"></i> 로그아웃</el-button>
            </div>
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
      this.$router.push('/')
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
    },
    myComments: function () {
      this.drawer = false
      this.$store.dispatch('getMyComments')
      this.$router.push({ name: 'MyComments' })
    }
  },
}
</script>

<style>

</style>