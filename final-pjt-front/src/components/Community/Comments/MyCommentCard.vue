<template>
  <div class="container">
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
}
</script>

<style>

</style>