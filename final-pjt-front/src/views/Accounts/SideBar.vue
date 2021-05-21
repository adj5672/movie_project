<template>
  <div class="container">
    <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
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
      <button @click="logout">로그아웃</button>
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
    }
  },
}
</script>

<style>

</style>