<template>
  <div>
    <el-button @click="drawer = true">
      <span v-if="!$store.state.isLogin">로그인</span>
      <span v-else>개인정보</span>
    </el-button>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-if="!$store.state.isLogin">
      <h2 class="my-3">로그인</h2>
      <Login @close-drawer="drawer = false"/>
    </el-drawer>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false"
      v-else>
      <div class="d-flex flex-column justify-content-between" style="height: 100%;">
        <div>
          <h1 class="mt-3">Hello, {{ $store.state.username }}</h1>
          <img src="@/assets/profile_image.png" alt="profile" style="width: 70%;">
        </div>
        <div>
          <el-button @click="myMovies" type="primary" style="width: 100%;">나만의 영화들</el-button>
          <br>
          <el-button @click="myReviews" type="success" style="width: 100%;">나의 리뷰들</el-button>
          <br>
          <el-button @click="logout" type="danger" style="width: 100%;">로그아웃</el-button>
        </div>
      </div>
    </el-drawer>

  </div>
</template>

<script>
import Login from '@/components/Accounts/Login'

export default {
  name: 'SideBar',
  data: function () {
    return {
      drawer: false,
    }
  },
  components: {
    Login,
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