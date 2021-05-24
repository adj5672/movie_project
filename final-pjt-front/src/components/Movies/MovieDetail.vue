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
          <!-- <p>평균 평점: {{ movie.rank_avg }}</p> -->
          <el-rate
            v-model="movie.rank_avg"
            disabled
            show-score
            text-color="#ff9900">
          </el-rate>
          <br>
          <div>
            <button v-if="$store.state.selectedMovie.isLike" @click="likeMovie">좋아요 취소</button>
            <button v-else @click="likeMovie">좋아요</button>
          </div>
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
        <Review v-for="(review, idx) in paginatedReviews" :review="review" :page="page" :movie="movie" :key="idx"/>
        <el-pagination
          class="text-center"
          background
          :page-size="5"
          layout="prev, pager, next"
          :total="totalPage"
          @current-change="movePage">
        </el-pagination>
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
  data: function () {
    return {
      page: 1,
    }
  },
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
    },
    paginatedReviews: function () {
      const start = (this.page - 1) * 5, // 1페이지면 0~5
            end = start + 5;
      return this.reviews.slice(start, end);
    },
    totalPage: function () {
      return this.reviews.length
    },
  },
  methods: {
    likeMovie: function () {
      this.$store.dispatch('likeMovie', this.movie)
    },
    movePage : function (page) {
      this.page = page
    }
  }
}
</script>

<style>

</style>