<template>
  <div class="col" @click="commentDetail" style="padding: 20px; min-width: 196px;">
    <div class="card card-hover h-100" style="cursor: pointer;">
      <div class="card-body shadow d-flex flex-column justify-content-between h-100">
        <div>
          <h3>{{ comment.review.title | titleTruncate }}</h3>
          <hr>
        </div>
        <p class="flex-fill my-auto">{{ comment.content | contentTruncate}}</p>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MyCommentCard',
  props: {
    comment: {
      type: Object,
    }
  },
  methods: {
    commentDetail: function () {
      this.$store.dispatch('selectComment', this.comment)
      this.$store.state.commentDialogVisible = true
    }
  },
  filters: {
    titleTruncate: function (text) {
      return _.truncate(text, {
        'length': 20
      })
    },
    contentTruncate: function (text) {
      return _.truncate(text, {
        'length': 50
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

p {
  font-family: 'Nanum Gothic', sans-serif;
  font-weight: 400;
}

</style>