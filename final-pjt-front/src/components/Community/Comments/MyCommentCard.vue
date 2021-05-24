<template>
  <div class="container" @click="commentDetail">
    <h3>{{ comment.review.title }}</h3>
    <hr>
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyCommentCard',
  props: {
    comment: {
      type: Object,
    }
  },
  methods: {
    commentDetail: function () {
      this.$store.dispatch('selectComment', this.comment)
      this.$store.state.commentDialogVisible = true
    }
  }
}
</script>

<style>

</style>