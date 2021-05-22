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
          <span v-for="(genre, idx) in movie.genres" :key="idx" class="me-2 fw-bold">#{{ genre.name }}</span>
          <p>평균 평점: {{ movie.rank_avg }}</p>
          <p>{{ movie.overview }}</p>
          
          <p>{{ movie.review_cnt }}명 중에 "{{ movie.tag_count }}"명의 사람들이 이 영화를 보고 <button>#{{ movie.most_tag }}</button> 을 느꼈습니다.</p>
          <hr>
        </div>
      </div>
      <hr>
      <div v-if="$store.state.isLogin">
        <h1>리뷰 작성</h1>
        <CreateReview/>
        <hr>
        <h1>전체 리뷰 조회</h1>
        <Review v-for="(review, idx) in reviews" :review="review" :key="idx"/>
      </div>
      <h2 v-else>로그인을 해야 리뷰를 작성, 조회 할 수 있습니다.</h2>
    </div>
  </el-dialog>
</template>

<script>
import CreateReview from '@/components/Community/Reviews/CreateReview'
import Review from '@/components/Community/Reviews/Review'

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