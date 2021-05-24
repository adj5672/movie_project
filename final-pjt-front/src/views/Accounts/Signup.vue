<template>
  <div id="Signup">
    <h1>회원가입</h1>
    <br>
    <div>
      <el-form label-position="top" label-width="100px" :model="credentials" class="d-flex flex-column align-items-center">
        <el-form-item label="아이디" class="d-flex flex-column align-items-start fw-bold">
          <el-input v-model="credentials.username" style="width: 400px;"></el-input>
        </el-form-item>
        <el-form-item label="비밀번호" class="d-flex flex-column align-items-start fw-bold">
          <el-input type="password" v-model="credentials.password" style="width: 400px;"></el-input>
        </el-form-item>
        <el-form-item label="비밀번호 재확인" class="d-flex flex-column align-items-start fw-bold">
          <el-input type="password" v-model="credentials.passwordConfirmation" style="width: 400px;"></el-input>
        </el-form-item>
        <el-form-item label="이메일" class="d-flex flex-column align-items-start fw-bold">
          <el-input v-model="credentials.email" style="width: 400px;" placeholder="선택입력"></el-input>
        </el-form-item>
        <el-form-item class="d-flex flex-column align-items-start fw-bold my-4">
          <el-button type="primary" @click="signup()" style="width: 400px; font-size: 1.1rem;">가입하기</el-button>
        </el-form-item>
      </el-form>
    </div>

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
        passwordConfirmation: null,
        email: '',
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
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#Signup {
  font-family: 'Jua', sans-serif;
}
</style>