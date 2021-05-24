<template>
  <div id="Sidebar">
    <el-button type="text" @click="drawer = true">
      <img src="@/assets/hamburger.png" alt="" style="height: 30px;">
    </el-button>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-if="!$store.state.isLogin"
      class="sidebarDrawer">
      <div class="d-flex flex-column justify-content-between my-3" style="height: 100%;">
        <div class="container">
          <h2 class="my-3 fw-bold">로그인</h2>
          <Login @close-drawer="drawer = false"/>
          <el-button @click="$router.push('Signup'); drawer=false"><i class="el-icon-user-solid"></i> 회원가입</el-button>
        </div>
        <div class="pb-3">
          <Moment/>
        </div>
      </div>
    </el-drawer>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-else>
      <div class="d-flex flex-column justify-content-between" style="height: 100%;" >
        <div>
          <div class="my-3">
            <img src="@/assets/profile_image.png" alt="profile" style="width: 50%;">
            <h1 class="fw-bold"><i class="el-icon-user"></i> {{ $store.state.username }}</h1>
          </div>
          <div class="d-flex flex-column align-items-center">
            <div class="d-flex flex-column flex-xl-row w-75">
              <el-button @click="myMovies" type="primary" class="w-100 me-xl-3"><i class="el-icon-video-camera-solid"></i> 나만의 영화</el-button>
              <br>
              <el-button @click="myReviews" type="success" class="w-100"><i class="el-icon-document"></i> 나의 리뷰</el-button>
            </div>
            <div class="d-flex flex-column flex-xl-row w-75 mt-xl-3">
              <br>
              <el-button @click="myComments" type="warning" class="w-100 me-xl-3"><i class="el-icon-chat-dot-round"></i> 나의 댓글</el-button>
              <br>
              <el-button  l-button @click="logout" type="danger" class="w-100"><i class="el-icon-switch-button"></i> 로그아웃</el-button>
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