<template>
  <div>
    <h1>회원가입</h1>
    <hr>
        <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <el-button :plain="true" @click="signup()">회원가입</el-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Signup",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          this.$message({
            message: '회원가입이 정상적으로 완료되었습니다.',
            type: 'success'
          });
          this.$router.push({ name: 'AllMovies' })
        })
        .catch(() => {
          this.$message.error('입력 항목을 다시 확인해주세요.')
        })
    }
  }
}
</script>

<style>

</style>