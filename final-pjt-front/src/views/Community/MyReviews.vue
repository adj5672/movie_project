<template>
  <div class="container">
    <h1 class="fw-bold">나의 리뷰</h1>
    <hr>
    <el-row :gutter="24">
      <el-col :span="8" v-for="(review, index) in myReviews" :key="index" class="my-4">
        <el-card :body-style="{ padding: '10px' }" shadow="hover">
          <MyReviewCard :review="review"/>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import MyReviewCard from '@/components/Community/Reviews/MyReviewCard'

export default {
  name: 'MyReviews',
  components: {
    MyReviewCard,
  },
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