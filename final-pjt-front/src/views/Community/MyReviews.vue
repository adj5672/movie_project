<template>
  <div id="MyReviews" style="margin-left: 15%; margin-right: 15%;">
    <h1 class="display-3"><i class="el-icon-document"></i> 나의 영화 리뷰</h1>
    <br>
    <div class="row row-cols-3 g-4">
      <MyReviewCard :review="review" v-for="(review, index) in myReviews" :key="index" />
    </div>
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Stylish&display=swap');

#MyReviews h1 {
  font-family: 'Black Han Sans', sans-serif;
}

</style>