<template>
  <div class="container">
    <h1>My_Reviews</h1>
    <br>
    <p v-for="(review, idx) in myReviews" :key="idx">{{ review }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyReviews',
  computed: {
    myReviews: function () {
      return this.$store.state.myReviews
    }
  },
  created: function () {
    this.$store.dispatch('getMyReviews')
  }
}
</script>

<style>

</style>