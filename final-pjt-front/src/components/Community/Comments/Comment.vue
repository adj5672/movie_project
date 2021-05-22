<template>
  <div>
    <h1>댓글</h1>
    <CreateComment/>
    <CommentList v-for="(comment, idx) in comments" :key="idx" :comment="comment"/>
  </div>
</template>

<script>
import CreateComment from '@/components/Community/Comments/CreateComment'
import CommentList from '@/components/Community/Comments/CommentList'

export default {
  name: 'Comment',
  components: {
    CreateComment,
    CommentList,
  },
  computed: {
    comments: function () {
      return this.$store.state.selectedReview.comment_set
    }
  }
}
</script>

<style>

</style>