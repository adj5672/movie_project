<template>
  <div class="d-flex justify-content-between my-3 w-100">
    <div class="my-auto d-flex flex-column w-75" style="min-width: 160px;">
      <div class="my-1">
        <span class="h6"><i class="el-icon-user"></i> {{ comment.user.username }}</span>
        <span v-if="$store.state.userId === comment.user.id" class="ms-2">
          <el-button @click="commentDetail" circle size="mini"><i class="el-icon-edit"></i></el-button>
          <el-button @click="deleteComment" circle size="mini"><i class="el-icon-delete"></i></el-button>
        </span>
      </div>
      <span>{{ comment.content }}</span>
    </div>
    <div class="d-flex flex-column" style="min-width: 135px;">
      <span>생성: {{ createdAt }}</span>
      <span>수정: {{ updatedAt }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentList',
  props: {
    comment: {
      type: Object,
    }
  },
  methods: {
    deleteComment: function () {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.$store.state.selectedMovie.id}/review/${this.$store.state.selectedReview.id}/comment/${this.comment.id}/`,
        headers: this.$store.state.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('selectReview', [this.$store.state.selectedMovie, this.$store.state.selectedReview])
        })
        .catch(err => {
          console.log(err)
        })
    },
    commentDetail: function () {
      this.$store.dispatch('selectComment', this.comment)
      this.$store.state.commentDialogVisible = true
    }
  },
  computed: {
    createdAt: function () {
      return this.$moment(this.comment.created_at).format('YY-MM-DD HH:mm')
    },
    updatedAt: function () {
      return this.$moment(this.comment.updated_at).format('YY-MM-DD HH:mm')
    },
  }
}
</script>

<style>

</style>
