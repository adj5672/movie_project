<template>
  <div @click="getReviewDetail" class="card card-hover p-3 mb-5" style="cursor: pointer;">
    <div class="d-flex flex-column justify-content-between align-items-start">
      <div class="d-flex align-items-center px-3 w-100 justify-content-between">
        <div class="d-flex flex-fill align-items-center">
          <h5 class="my-auto fw-bold" style="width: 40%;">{{ review.title | titleTruncate }}</h5>
          <h6 class="my-auto mx-1"><i class="el-icon-user"></i> {{ review.user.username }} ·</h6>
          <h6 class="my-auto mx-1"><i class="el-icon-chat-dot-round"></i> ({{ review.comment_cnt }}) ·</h6>
          <el-rate
            v-model="review.rank"
            disabled
            class="my-2 mx-1">
          </el-rate>
          <div class="my-auto">
            <h5 class="my-auto" v-if="review.tags === '기쁨'">· 😀</h5>
            <h5 class="my-auto" v-else-if="review.tags === '슬픔'">· 😥</h5>
            <h5 class="my-auto" v-else-if="review.tags === '짜증'">· 🤬</h5>
            <h5 class="my-auto" v-else-if="review.tags === '심심'">· 🥱</h5>
            <h5 class="my-auto" v-else>· 😍</h5>
          </div>
        </div>

        <div class="my-auto">
          <div>작성 : {{ createdAt }}</div>
          <div>수정 : {{ updatedAt }}</div>
        </div>
      </div>
      <p class="my-2 text-start p-3">{{ review.content | contentTruncate }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

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

<style>
  .card-hover:hover {
    background: #eeee;
  }
</style>