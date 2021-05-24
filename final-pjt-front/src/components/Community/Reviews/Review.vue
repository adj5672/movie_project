<template>
  <div @click="getReviewDetail" class="card card-hover p-2" style="cursor: pointer;">
    <div class="d-flex justify-content-between">
      <div class="flex-column">
        <h5 class="m-0">{{ review.title }}</h5>
        <hr class="my-2">
        <el-rate
          v-model="review.rank"
          disabled
          class="mb-1">
        </el-rate>
        <div>Tag: {{ review.tags }}</div>
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
      return this.$moment(this.review.created_at).format('YY-MM-DD HH:mm')
    },
    updatedAt: function () {
      return this.$moment(this.review.updated_at).format('YY-MM-DD HH:mm')
    }
  }
}
</script>

<style>
  .card-hover:hover {
    background: #eeee;
  }
</style>