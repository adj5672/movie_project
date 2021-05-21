<template>
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="120px" class="demo-ruleForm container my-4">
    <el-form-item label="username" prop="pass">
      <el-input type="username" v-model="credentials.username" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="password" prop="checkPass">
      <el-input type="password" v-model="credentials.password" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="login">로그인</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          const token = res.data.token
          this.$store.dispatch('logIn', token)
          this.$emit('close-drawer')
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>