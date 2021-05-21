<template>
  <div>
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