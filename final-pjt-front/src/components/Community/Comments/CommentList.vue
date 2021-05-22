<template>
  <div>
    <span>{{ comment.user }} : {{ comment.content }}</span>
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
