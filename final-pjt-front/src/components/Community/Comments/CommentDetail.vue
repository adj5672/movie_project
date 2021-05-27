<template>
  <div>
    <el-dialog
      title=""
      :visible.sync="$store.state.commentDialogVisible"
      width="900px"
      center
      style="min-width: 350px;">
      <div class="container">
        <h1 class="Sans">댓글 수정</h1>
        <hr>
        <el-form ref="form" :model="comment" label-width="120px" labelPosition="left">
          <el-input type="textarea" v-model="comment.content"></el-input>
          <div class="d-flex justify-content-between">
            <div>
              <el-button @click="updateComment" type="primary" circle><i class="el-icon-edit"></i></el-button>
              <el-button @click="deleteComment" type="danger" circle><i class="el-icon-delete"></i></el-button>  
            </div>
            <div>
              <p class="my-auto">작성 : {{ createdAt }}</p>
              <p class="my-auto">수정 : {{ updatedAt }}</p>
            </div>
          </div>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentDetail',
  computed: {
    comment: function () {
      return this.$store.state.selectedComment
    },
    createdAt: function () {
      return this.$moment(this.comment.created_at).format('YY-MM-DD HH:mm')
    },
    updatedAt: function () {
      return this.$moment(this.comment.updated_at).format('YY-MM-DD HH:mm')
    },

  },
  methods: {
    updateComment: function () {
      axios({
        method: 'PUT',
        url: `http://127.0.0.1:8000/community/review/${this.comment.review.id}/comment/${this.comment.id}/`,
        data: this.comment,
        headers: this.$store.state.config
      })
        .then(() => {
          this.$store.dispatch('selectReview', [this.comment.review.movie, this.comment.review])
          this.$store.dispatch('getMyComments')
          this.$store.state.commentDialogVisible = false
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment: function () {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/review/${this.comment.review}/comment/${this.comment.id}/`,
        headers: this.$store.state.config
      })
        .then(() => {
          this.$store.dispatch('selectReview', [this.comment.review.movie, this.comment.review])
          this.$store.dispatch('getMyComments')
          this.$store.state.commentDialogVisible = false
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
  
}
</script>

<style>

</style>