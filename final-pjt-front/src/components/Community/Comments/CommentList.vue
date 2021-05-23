<template>
  <div>
    <span>{{ comment.user.username }} : {{ comment.content }}</span>
    <span>생성: {{ comment.created_at }} 수정: {{ comment.updated_at }}</span>
    <span v-if="$store.state.userId === comment.user.id">
      <button>수정</button>
      <button @click="deleteComment">삭제</button>
    </span>
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
    }
  }
}
</script>

<style>

</style>
