<template>
  <div>
    <el-form ref="form" :model="form" label-width="120px" labelPosition="left" class="d-flex justify-content-end align-items-center mb-3">
      <el-input @keyup.enter="createComment" type="textarea" v-model="form.content" class="my-auto me-3"></el-input>
      <el-button class="Sans" type="primary" @click="createComment">작성</el-button>
    </el-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateComment',
  data: function () {
    return {
      form: {
        content: null,
      }
    }
  },
  methods: {
    createComment: function () {
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.$store.state.selectedReview.id}/`,
        data: this.form,
        headers: this.$store.state.config
      })
        .then(() => {
          this.$store.dispatch('selectReview', [this.$store.state.selectedMovie, this.$store.state.selectedReview])
          this.$message({
            message: '댓글이 작성되었습니다.',
            type: 'success'
          })
          this.form.content = null
        })
        .catch(err => {
          console.log(err)
          this.$message.error('입력 항목을 다시 확인해주세요.')
        })
    }
  }
}
</script>

<style>

</style>
