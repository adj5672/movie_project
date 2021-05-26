<template>
  <el-form status-icon ref="ruleForm" label-width="120px" label-position="top" class="demo-ruleForm container my-3" style="width: 80%;">
    <el-form-item label="" prop="pass">
      <el-input type="username" v-model="credentials.username" autocomplete="off" placeholder="아이디"></el-input>
    </el-form-item>
    <el-form-item label="" prop="checkPass">
      <el-input type="password" v-model="credentials.password" autocomplete="off" placeholder="비밀번호"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="login" style="width: 100%; font-size: 1.1rem;"><i class="el-icon-switch-button"></i> 로그인</el-button>
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
        .catch(() => {
          this.$message.error('입력 정보를 다시 확인해주세요.')
        })
    }
  }
}
</script>

<style>

</style>