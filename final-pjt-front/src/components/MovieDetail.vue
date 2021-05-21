<template>
  <el-dialog
    :title="''"
    :visible.sync="$store.state.centerDialogVisible"
    width="90%"
    center>
    <div class="container">
      <div class="d-flex">
        <img :src="posterSrc" alt="image" style="width: 40%;">
        <div class="p-3">
          <h1>{{ movie.title }}</h1>
          <span>{{ movie.release_date }}</span>
          <br>
          <span>장르</span>
          <!-- <p>장르</p> -->
          <p>{{ movie.overview }}</p>
          <p>'n'명의 사람들이 이 영화를 보고 <button>#기쁨</button> 을 느꼈습니다.</p>
          <hr>
        </div>
      </div>
      <hr>
      <h1>리뷰 작성</h1>
      <CreateReview/>
      <hr>
      <h1>전체 리뷰 조회</h1>
      <Review v-for="(review, idx) in reviews" :review="review" :key="idx"/>
    </div>
  </el-dialog>
</template>

<script>
import CreateReview from '@/components/CreateReview'
import Review from '@/components/Review'

export default {
  name: 'MovieDetail',
  components: {
    CreateReview,
    Review,
  },
  computed: {
    movie: function () {
      return this.$store.state.selectedMovie
    },
    posterSrc: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
    reviews: function () {
      return this.$store.state.reviews
    }
  },
}
</script>

<style>

</style>