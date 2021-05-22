<template>
  <div>
    <span>{{ comment.user.username }} : {{ comment.content }}</span>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    comment: {
      type: Object,
    }
  }
}
</script>

<style>

</style>
