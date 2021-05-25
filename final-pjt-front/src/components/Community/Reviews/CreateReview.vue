<template>
  <el-form ref="form" :model="form" label-width="120px" labelPosition="left">
    <div class="d-flex my-3"> 
      <span class="align-self-center">평점</span>
      <el-rate class="my-auto ms-4" v-model="form.rank"></el-rate>
      <el-select v-model="form.tags" class="ms-3" placeholder="please select your zone" style="width: 80px;">
        <el-option label="기쁨" value="기쁨"></el-option>
        <el-option label="슬픔" value="슬픔"></el-option>
        <el-option label="짜증" value="짜증"></el-option>
        <el-option label="심심" value="심심"></el-option>
        <el-option label="사랑" value="사랑"></el-option>
      </el-select>
    </div>
    <el-form-item label="제목" label-width="50px">
      <el-input v-model="form.title"></el-input>
    </el-form-item>
    <el-form-item label="내용" label-width="50px">
      <el-input type="textarea" v-model="form.content" :autosize="{ minRows: 6, maxRows: 6}"></el-input>
    </el-form-item>
    <el-form-item class="w-100 d-flex justify-content-end">
      <el-button class="Sans" type="primary" @click="createReview">작성</el-button>
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
        .then(() => {
          this.$store.dispatch('selectMovie', this.$store.state.selectedMovie)
          this.$emit('is-create')
        })
        .catch(err => {
          console.log(err)
        })
      this.form = {
      rank: 0,
      tags: '기쁨',
      title: null,
      content: null,
      }
    }
  }
}
</script>

<style>
  .el-form > div {
    margin-bottom: 1rem;
  }
</style>