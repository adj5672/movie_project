<template>
  <div style="padding: 10px;" @click="getReviewDetail" class="h-100">
    <h4 class="fw-bold">{{ review.movie.title }}</h4>
    <hr>
    <el-rate
      v-model="review.rank"
      disabled>
    </el-rate>
    <br>
    <h5>{{ review.title }}</h5>
    <p>{{ review.content | stringTruncate }}</p>
    <p>{{ review.tags }}</p>
    <p>댓글 ({{ review.comment_cnt }})</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MyReviewCard',
  props: {
    review: {
      type: Object,
    }
  },
  methods: { 
    getReviewDetail: function () {
      this.$store.dispatch('selectReview', [this.review.movie, this.review])
      this.$store.state.reviewDialogVisible = true
    }
  },
  filters: {
    stringTruncate: function (text) {
      return _.truncate(text, {
        'length': 200
      })
    }
  }
}
</script>

<style>

</style>