<template>
  <div>
    <el-form ref="form" :model="form" label-width="120px" labelPosition="left">
      <el-form-item label="content" prop="desc">
      <el-input type="textarea" v-model="form.content"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="createComment">Create</el-button>
      </el-form-item>
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
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
      this.$store.dispatch('selectReview', [this.$store.state.selectedMovie, this.$store.state.selectedReview])
    }
  }
}
</script>

<style>

</style>