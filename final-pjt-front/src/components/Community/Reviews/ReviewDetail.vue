<template>
  <div>
    <el-dialog
      title=""
      :visible.sync="$store.state.reviewDialogVisible"
      width="90%"
      center>
      <div class="container" v-if="review.user">
        <h1>{{ review.movie.title }}</h1>
        <hr>
        <el-form v-if="$store.state.userId === review.user.id" ref="form" :model="review" label-width="120px" labelPosition="left">
          <el-rate v-model="review.rank"></el-rate>
          <el-form-item label="Tag">
            <el-select v-model="review.tags" placeholder="please select your zone">
              <el-option label="기쁨" value="기쁨"></el-option>
              <el-option label="슬픔" value="슬픔"></el-option>
              <el-option label="짜증" value="짜증"></el-option>
              <el-option label="심심" value="심심"></el-option>
              <el-option label="사랑" value="사랑"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="Title">
            <el-input v-model="review.title"></el-input>
          </el-form-item>
          <el-form-item label="Content">
            <el-input type="textarea" v-model="review.content"></el-input>
          </el-form-item>
          <div>생성 시각: {{ review.created_at }}</div>
          <div>수정 시각: {{ review.updated_at }}</div>
          <el-button type="primary" @click="updateReview">수정</el-button>
          <el-button type="danger" @click="deleteReview">삭제</el-button>
        </el-form>
        <el-form v-else>
          <h3>Title: {{ review.title }}</h3>
          <!-- <p>rank: {{ review.rank }}</p> -->
          <el-rate
            v-model="review.rank"
            disabled
            text-color="#ff9900">
          </el-rate>
          <p>Tag: {{ review.tags }}</p>
          <p>Content: {{ review.content }}</p>
          <div>생성: {{ review.created_at }}</div>
          <div>수정: {{ review.updated_at }}</div>
        </el-form>
        <hr>
        <Comment/>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Community/Comments/Comment'


export default {
  name: 'ReviewDetail',
  components: {
    Comment,
  },
  computed: {
    review: function () {
      return this.$store.state.selectedReview
    },
  },
  methods: {
    // 리뷰 삭제
    deleteReview: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.review.id}/`,
        headers: this.$store.state.config,
      })
        .then(() => {
          this.$store.dispatch('selectMovie', this.$store.state.selectedMovie)
          this.$store.state.reviewDialogVisible = false
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 리뷰 수정
    updateReview: function() {
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.review.id}/`,
        data: this.review,
        headers: this.$store.state.config,
      })
        .then(() => {
          this.$store.dispatch('selectMovie', this.$store.state.selectedMovie)
          this.$store.state.reviewDialogVisible = false
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
}
</script>

<style>

</style>