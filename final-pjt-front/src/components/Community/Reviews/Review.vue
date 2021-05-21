<template>
  <div>
    <span>{{ review.tags }}</span>
    <p>{{ review.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'Review',
  props: {
    review: {
      type: Object
    }
  }
}
</script>

<style>

</style>