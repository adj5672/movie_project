<template>
  <el-dialog
    :title="''"
    :visible.sync="$store.state.centerDialogVisible"
    width="90%"
    center>
    <div class="position-relative">
    </div>
    <!-- <img class="position-absolute top-0 start-0" :src="posterSrc" alt="image" style="height:100%; width:100%; opacity:0.3; z-index:0;"> -->
    <div class="container">
      <div class="d-flex row" style="height:500px">
        <div class="col-4" style="height:100%;">
          <img :src="posterSrc" alt="image" style="height:100%; opacity:1;">
        </div>
        <div class="card p-3 col" >
          <div class="d-flex">
            <h1 class="m-0">{{ movie.title }}</h1>
            <div>
              <button class="btn" v-if="$store.state.selectedMovie.isLike" @click="likeMovie"><font-awesome-icon style="color:crimson;" :icon="['fas','heart']"/></button>
              <el-tooltip v-else content="나만의 영화에 추가하세요" placement="bottom" effect="light">
                <button class="btn" @click="likeMovie"><font-awesome-icon :icon="['far','heart']"/></button>
              </el-tooltip>
            </div>
          </div>
          <span>개봉: {{ movie.release_date }}</span>
          <br>
          <div>
            <span v-for="(genre, idx) in movie.genres" :key="idx" class="me-2 fw-bold">#{{ genre.name }}</span>
          </div>
          <!-- <p>평균 평점: {{ movie.rank_avg }}</p> -->
          <el-rate
            v-model="movie.rank_avg"
            disabled
            show-score
            text-color="#ff9900"
            class="mt-2"
          >
          </el-rate>
          <br>
          <h5>개요</h5>
          <p v-if="movie.overview" style="font-style: italic;">{{ movie.overview }}</p>
          <p v-else style="font-style: italic;">해당 영화는 줄거리가 없습니다...</p>
          <p>{{ movie.review_cnt }}명 중에 "<button class="btn p-1 fs-5 fw-bold" style="color:orange">{{ movie.tag_count }}</button>"명의 사람들이 이 영화를 보고 <button class="btn p-1 fs-5 fw-bold" style="color:orange">#{{ movie.most_tag }}</button> 을 느꼈습니다.</p>
        </div>
      </div>
      <hr>
      <div v-if="$store.state.isLogin">
        <h3>리뷰 작성</h3>
        <CreateReview/>
        <hr>
        <h3>이 영화의 리뷰</h3>
          <p v-if="!reviews.length">아직 리뷰가 없습니다. 처음으로 리뷰를 작성해보세요...</p>
          <Review class="m-1" v-for="(review, idx) in paginatedReviews" :review="review" :page="page" :movie="movie" :key="idx"/>
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