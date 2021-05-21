<template>
  <el-form ref="form" :model="form" label-width="120px" labelPosition="left">
    <w-rating v-model="form.rank" color="yellow"></w-rating>
    <el-form-item label="Tag">
      <el-select v-model="form.tags" placeholder="please select your zone">
        <el-option label="기쁨" value="기쁨"></el-option>
        <el-option label="슬픔" value="슬픔"></el-option>
        <el-option label="짜증" value="짜증"></el-option>
        <el-option label="심심" value="심심"></el-option>
        <el-option label="사랑" value="사랑"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Title">
      <el-input v-model="form.title"></el-input>
    </el-form-item>
    <el-form-item label="Content">
      <el-input type="textarea" v-model="form.content"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="createReview">Create</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CreateReview',
  data: function () {
    return {
      form: {
        rank: 0,
        tags: '기쁨',
        title: null,
        content: null,
      }
    }
  },
  methods: {
    createReview: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/`,
        data: this.form,
        headers: this.$store.state.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('getReviews')
          this.form = {
          rank: 0,
          tags: '기쁨',
          title: null,
          content: null,
          }
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