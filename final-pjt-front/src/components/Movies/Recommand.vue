<template>
  <div class="my-3">
    <div class="mb-5">
      <vue-feedback-reaction :labels="labels" v-model="value" emojiWidth='60px' emojiHeight='60px' />
    </div>
    <h1 class="question display-5 fw-bold">이런 영화는 어떠세요?</h1>
    <carousel-3d class="p-3" v-if="$store.state.movies.tag_movies.length" :display=7 :space=250 :width=280 :height=400 :controls-visible="true" @after-slide-change="movieIndex">
      <slide v-for="(movie, i) in tagMovies" :index="i" :key="i" class="rounded-3 border">
        <TagCarousel :movie="movie" style="cursor: pointer" :index="i" :centerIndex="centerIndex"/>
        <button class="btn position-absolute top-0 end-0" :style="heartVisible(movie)"><font-awesome-icon size="lg" style="color:crimson;" :icon="['fas','heart']"/></button>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import TagCarousel from '@/components/Movies/Carousel/TagCarousel'
import _ from 'lodash'
import { VueFeedbackReaction } from 'vue-feedback-reaction'

export default {
  name: 'Recommand',
  data: function () {
    return {
      centerIndex: 0,
      color: '#ffc168',
      value: 1,
      labels: ['짜증나', '슬퍼요', '심심해', '기뻐요', '로맨스'],
    }
  },
  components: {
    TagCarousel,
    VueFeedbackReaction,
  },
  methods: {
    getTagMovies: function () {
      this.$store.dispatch('getTagMovies', this.selectTag)
      if (this.selectTag === '기쁨') {
        this.color = '#FFE13C' // 노랑
      } else if ( this.selectTag === '슬픔') {
        this.color = '#FF9DFF' // 보라
      } else if ( this.selectTag === '짜증') {
        this.color = '#FF8C8C' // 빨강
      } else if ( this.selectTag === '심심') {
        this.color = '#787878' // 검정 or 갈색 
      } else if ( this.selectTag === '사랑') {
        this.color = '#EE82EE' // 핑크
      } 
      this.$emit('changeTag', this.selectTag)
    },
    movieIndex: function (data) {
      this.centerIndex = data
    },
    heartVisible: function (movie) {
      var tmp = 0
      _.forEach((this.myMovies), function(myMovie) {
        if (movie.id === myMovie.id) {
          tmp = 1
        }
      })
      if (tmp === 1) {
        return { visibility: 'visible' }
      } else {
        return { visibility: 'hidden' }
      }
    },
  },
  computed: {
    tagMovies: function () {
      return this.$store.state.movies.tag_movies
    },
    myMovies: function () {
      return this.$store.state.myMovies
    },
    borderColor: function () {
      return {'border' : `5px solid ${this.color}`}
    },
    backgroundColor: function () {
      return {'color': `${this.color}`}
    },
    selectTag: function () {
      if (this.value === '1') {
        return '짜증'
      } else if (this.value === '2') {
        return '슬픔'
      } else if (this.value === '3') {
        return '심심'
      } else if (this.value === '4') {
        return '기쁨'
      } else {
        return '사랑'
      }
    }
  },
  created: function () {
    this.getTagMovies()
    this.$store.dispatch('getMyMovies')
  },
  watch: {
    value: function () {
      // console.log(this.selectTag)
      this.$store.dispatch('getTagMovies', this.selectTag)
      if (this.selectTag === '기쁨') {
        this.$store.state.selectedColor = '#FFE13C' // 노랑
      } else if ( this.selectTag === '슬픔') {
        this.$store.state.selectedColor = '#648CFF' // 파랑
      } else if ( this.selectTag === '짜증') {
        this.$store.state.selectedColor = '#D76464' // 빨강
      } else if ( this.selectTag === '심심') {
        this.$store.state.selectedColor = '#A8F552' // 초록
      } else if ( this.selectTag === '사랑') {
        this.$store.state.selectedColor = '#EE82EE' // 핑크
      } 
      // console.log(this.color)
      this.$emit('changeTag', this.selectTag)
    },
  }
}
</script>

<style>

</style>