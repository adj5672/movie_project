<template>
  <div @click="getReviewDetail" class="card">
    <span>{{ review.rank }}점</span>
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
    },
    movie: {
      type: Object
    }
  },
  methods: { 
    getReviewDetail: function () {
      this.$store.dispatch('selectReview', [this.movie, this.review])
      this.$store.state.reviewDialogVisible = true
    }
  }
}
</script>

<style>

</style>