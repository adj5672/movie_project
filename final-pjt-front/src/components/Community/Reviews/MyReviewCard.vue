<template>
  <div class="col" @click="getReviewDetail" style="padding: 20px; min-width: 196px;">
    <div class="card card-hover h-100" style="cursor: pointer;">
      <div class="card-body shadow d-flex flex-column justify-content-between h-100">
        <div>
          <h3 class="fw-bold my-0">{{ review.movie.title }}</h3>
          <hr>
          <div class="d-flex justify-content-center align-items-center my-2">
            <el-rate
              v-model="review.rank"
              disabled
              class="my-0 me-2">
            </el-rate>
            <div>
              <h5 class="my-auto" v-if="review.tags === '기쁨'"> 😀</h5>
              <h5 class="my-auto" v-else-if="review.tags === '슬픔'"> 😥</h5>
              <h5 class="my-auto" v-else-if="review.tags === '짜증'"> 🤬</h5>
              <h5 class="my-auto" v-else-if="review.tags === '심심'"> 🥱</h5>
              <h5 class="my-auto" v-else> 😍</h5>
            </div>
            <!-- <p>{{ review.tags }}</p> -->
          </div>
          <h5 class="my-3 fw-bold" id="reviewTitle">{{ review.title | titleTruncate }}</h5>
          <p>{{ review.content | contentTruncate }}</p>
        </div>
        <p><i class="el-icon-chat-dot-round"></i> ({{ review.comment_cnt }})</p>
      </div>
    </div>
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
    titleTruncate: function (text) {
      return _.truncate(text, {
        'length': 25
      })
    },
    contentTruncate: function (text) {
      return _.truncate(text, {
        'length': 220
      })
    },
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Sunflower:wght@500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');

h3 {
  font-family: 'Sunflower', sans-serif;
  font-weight: 500
}

#reviewTitle {
  font-family: 'Nanum Gothic', sans-serif;
  font-weight: 800;
}

p {
  font-family: 'Nanum Gothic', sans-serif;
  font-weight: 400;
}

</style>