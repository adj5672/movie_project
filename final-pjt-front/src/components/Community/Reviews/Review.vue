<template>
  <div @click="getReviewDetail" class="card">
    <div class="d-flex justify-content-between">
      <div class="flex-column">
        <el-rate
          v-model="review.rank"
          disabled>
        </el-rate>
        <div>Tag: {{ review.tags }}</div>
        <div>Title: {{ review.title }}</div>
      </div>
      <div>
        <div>작성자: {{ review.user.username }}</div>
        <div>생성 시각: {{ createdAt }}</div>
        <div>수정 시각: {{ updatedAt }}</div>
      </div>
    </div>
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
    },
    page: {
      type: Number,
    }
  },
  methods: { 
    getReviewDetail: function () {
      this.$store.dispatch('selectReview', [this.movie, this.review])
      this.$store.state.reviewDialogVisible = true
    }
  },
  computed: {
    createdAt: function () {
      return this.$moment(this.review.created_at).format('YY-MM-DD HH:mm:ss')
    },
    updatedAt: function () {
      return this.$moment(this.review.updated_at).format('YY-MM-DD HH:mm:ss')
    }
  }
}
</script>

<style>

</style>