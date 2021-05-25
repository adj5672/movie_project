<template>
  <el-dialog
    :title="''"
    :visible.sync="$store.state.centerDialogVisible"
    width="90%"
    center
    id="MovieDetail"
    style="min-width: 1100px;">
    <div class="px-5">
      <!-- 영화 포스터 및 소개 카드 -->
      <div class="d-flex" style="height: 500px">
        <!-- 영화 포스터 -->
        <div class="mx-2" style="height: 100%;">
          <img :src="posterSrc" alt="image" style="height:100%; opacity:1;" class="rounded-3">
        </div>
        <!-- 소개 카드 -->
        <div class="card p-4 d-flex flex-fill flex-column justify-content-between" >
          <div>
            <div class="d-flex">
              <div class="d-flex align-items-center">
                <h1 class="my-auto fw-bold" id="MovieTitle" style="color: black">{{ movie.title }}</h1>
                <div>
                  <button class="btn" v-if="$store.state.selectedMovie.isLike" @click="likeMovie"><font-awesome-icon style="color:crimson;" size="lg" :icon="['fas','heart']"/></button>
                  <el-tooltip v-else content="나만의 영화에 추가하세요" placement="bottom" effect="light">
                    <button class="btn" @click="likeMovie"><font-awesome-icon size="lg" :icon="['far','heart']"/></button>
                  </el-tooltip>
                </div>
              </div>
            </div>
            <div class="d-flex align-items-center my-2">
              <span>{{ movie.release_date }}</span>
              <div class="mx-3">
                <span v-for="(genre, idx) in movie.genres" :key="idx" class="me-2 fw-bold text-primary">#{{ genre.name }}</span>
              </div>
            </div>
            <el-rate
              v-model="movie.rank_avg"
              disabled
              show-score
              text-color="#ff9900"
              class="my-2"
            >
            </el-rate>
            <h5 class="fw-bold mt-3">줄거리</h5>
            <p v-if="movie.overview">{{ movie.overview }}</p>
            <p v-else style="font-style: italic;">해당 영화는 줄거리가 없습니다...</p>
          </div>
          <p class="my-0" id="mostTag"><span class="fs-5 p-1 fw-bold">{{ movie.review_cnt }}</span>명 중에 "<span class="fs-5 p-1 fw-bold" style="color:orange">{{ movie.tag_count }}</span>"명의 사람들이 이 영화를 보고 <span class="p-1 fs-5 fw-bold" style="color:orange">#{{ movie.most_tag }}</span>을 느꼈습니다.</p>
        </div>
      </div>
      <hr>

      <div v-if="$store.state.isLogin">
        <!-- 리뷰 작성-->
        <div v-show="isCreate">
          <div class="d-flex justify-content-between my-2 align-items-center">
            <h3 class="fw-bold my-auto">리뷰 작성</h3>
            <el-button type="text" class="mx-3 text-dark" size="medium" @click="isCreate = !isCreate">X</el-button>
          </div>
          <CreateReview @is-create="writeReview"/>
          <hr>
        </div>
        <!-- 영화에 달린 리뷰들 -->
        <div class="d-flex align-items-center justify-content-between mb-3">
          <h3 class="fw-bold my-auto me-4">이 영화의 리뷰 ({{ movie.review_cnt }})</h3>
          <el-button style="font-size: 1.1rem; font-weight: bold;" @click="isCreate = !isCreate"><i class="el-icon-document"></i> 리뷰 작성</el-button>
        </div>
        <p v-if="!reviews.length">아직 리뷰가 없습니다. 처음으로 리뷰를 작성해보세요...</p>
        <div v-else>
          <Review class="m-1" v-for="(review, idx) in paginatedReviews" :review="review" :page="page" :movie="movie" :key="idx"/>
          <el-pagination
            class="text-center mb-4"
            background
            :page-size="5"
            layout="prev, pager, next"
            :total="totalPage"
            @current-change="movePage">
          </el-pagination>
        </div>
      </div>
      <h2 v-else class="text-center">로그인을 하면 리뷰를 조회 및 작성 할 수 있습니다.</h2>
    </div>
  </el-dialog>
</template>

<script>
import CreateReview from '@/components/Community/Reviews/CreateReview'
import Review from '@/components/Community/Reviews/Review'
import _ from 'lodash'

export default {
  name: 'MovieDetail',
  data: function () {
    return {
      page: 1,
      isCreate: false,
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
    movePage: function (page) {
      this.page = page
    },
    writeReview: function () {
      this.isCreate = !this.isCreate
      this.$message({
          message: '성공적으로 리뷰가 작성되었습니다.',
          type: 'success'
      })
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
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;900&display=swap');

#mostTag {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 400;
}

#MovieTitle {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
}
</style>