<template>
  <div>
    <span>{{ review.tags }}</span>
    <p @click="getReviewDetail">{{ review.title }}</p>
    <div class="text-end">
      <button @click="deleteReview">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
    deleteReview: function() {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.movie.id}/review/${this.review.id}/`,
        headers: this.$store.state.config,
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('getReviews')
        })
        .catch(err => {
          console.log(err)
        })
    },
    getReviewDetail: function () {
      this.$store.state.reviewDialogVisible = true
      this.$store.dispatch('selectReview', [this.movie, this.review])
    }
  }
}
</script>

<style>

</style>