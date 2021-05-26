<template>
  <div>
    <el-dialog
      title=""
      :visible.sync="$store.state.reviewDialogVisible"
      width="900px"
      center
      style="min-width: 650px;">
      <div class="container" v-if="review.user">
        <h1 class="fw-bold SansBold text-dark">{{ review.movie.title }}</h1>
        <hr>
        <!-- 리뷰 수정 Form -->
        <el-form v-if="$store.state.userId === review.user.id" ref="form" :model="review" label-width="120px" labelPosition="left">
          <div class="d-flex justify-content-between">
            <div class="d-flex my-auto">
              <span class="align-self-center">평점</span>
              <el-rate v-model="review.rank" class="my-auto ms-4"></el-rate>
              <el-select v-model="review.tags" class="ms-3" placeholder="please select your zone" style="width: 80px;">
                <el-option label="기쁨" value="기쁨"></el-option>
                <el-option label="슬픔" value="슬픔"></el-option>
                <el-option label="짜증" value="짜증"></el-option>
                <el-option label="심심" value="심심"></el-option>
                <el-option label="사랑" value="사랑"></el-option>
              </el-select>
            </div>
            <div class="my-auto">
              <div class="Sans">작성 : {{ createdAt }}</div>
              <div class="Sans">수성 : {{ updatedAt }}</div>
            </div>
          </div>
          <el-form-item label="제목" label-width="50px">
            <el-input v-model="review.title"></el-input>
          </el-form-item>
          <el-form-item label="내용" label-width="50px">
            <el-input type="textarea" v-model="review.content" :autosize="{ minRows: 6, maxRows: 6}"></el-input>
          </el-form-item>
          <div class="w-100 d-flex justify-content-end">
            <el-button type="primary" circle @click="updateReview"><i class="el-icon-edit"></i></el-button>
            <el-button type="danger" circle @click="deleteReview"><i class="el-icon-delete"></i></el-button>
          </div>
        </el-form>
        <!-- 상세 리뷰 내용 -->
        <el-form v-else>
          <div class="d-flex justify-content-between">
            <h3 class="my-auto fw-bold Jua">{{ review.title }}</h3>
            <div>
              <div class="Sans">작성 : {{ createdAt }}</div>
              <div class="Sans">수성 : {{ updatedAt }}</div>
            </div>
          </div>
          <div class="d-flex mb-4">
            <el-rate
              v-model="review.rank"
              disabled
              text-color="#ff9900">
            </el-rate>
            <div class="my-auto">
              <h5 class="my-auto" v-if="review.tags === '기쁨'">· 😀</h5>
              <h5 class="my-auto" v-else-if="review.tags === '슬픔'">· 😥</h5>
              <h5 class="my-auto" v-else-if="review.tags === '짜증'">· 🤬</h5>
              <h5 class="my-auto" v-else-if="review.tags === '심심'">· 🥱</h5>
              <h5 class="my-auto" v-else>· 😍</h5>
            </div>
          </div>
          <div class="Sans">{{ review.content }}</div>
        </el-form>
        <hr>
        <!-- 댓글 Component -->
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
    createdAt: function () {
      return this.$moment(this.review.created_at).format('YY-MM-DD HH:mm')
    },
    updatedAt: function () {
      return this.$moment(this.review.updated_at).format('YY-MM-DD HH:mm')
    }
  },
  methods: {
    // 리뷰 삭제
    deleteReview: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.review.movie.id}/review/${this.review.id}/`,
        headers: this.$store.state.config,
      })
        .then(() => {
          this.$store.dispatch('selectMovie', this.review.movie)
          this.$store.dispatch('getMyReviews')
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
        url: `http://127.0.0.1:8000/community/${this.review.movie.id}/review/${this.review.id}/`,
        data: this.review,
        headers: this.$store.state.config,
      })
        .then(() => {
          this.$store.dispatch('selectMovie', this.review.movie)
          this.$store.dispatch('getMyReviews')
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