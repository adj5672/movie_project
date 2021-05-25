<template>
  <div class="my-3">
    <div class="mb-5">
      <el-select class="p-1 me-3" id="tag_select" v-model="selectTag">
        <el-option value="기쁨">기쁨</el-option>
        <el-option value="슬픔">슬픔</el-option>
        <el-option value="짜증">짜증</el-option>
        <el-option value="심심">심심</el-option>
        <el-option value="사랑">사랑</el-option>
      </el-select>
      <vue-reaction-emoji :reaction="reaction" :is-active="isActive" :is-disabled="isDisabled"/>
      <button class="btn color" @click="getTagMovies" :style="backgroundColor">선택</button>
    </div>
    <carousel-3d class="p-3 color" :style="borderColor" v-if="$store.state.movies.tag_movies.length" :display=7 :space=250 :width=280 :height=400 :controls-visible="true" @after-slide-change="movieIndex">
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
import { VueReactionEmoji } from 'vue-feedback-reaction'

export default {
  name: 'Recommand',
  data: function () {
    return {
      selectTag: '기쁨',
      centerIndex: 0,
      color: '#ffc168',
      reaction: {
        type: String,
        default: 'natural',
        validator: (v) => (['hate', 'disappointed', 'natural', 'good', 'excellent'].includes(v))
      },
      isActive: false,
      isDisabled: false
    }
  },
  components: {
    TagCarousel,
    VueReactionEmoji,
  },
  methods: {
    getTagMovies: function () {
      this.$store.dispatch('getTagMovies', this.selectTag)
      if (this.selectTag === '기쁨') {
        this.color = '#ffc168' // 노랑
      } else if ( this.selectTag === '슬픔') {
        this.color = '#8e43e7' // 보라
      } else if ( this.selectTag === '짜증') {
        this.color = '#b84592' // 빨강
      } else if ( this.selectTag === '심심') {
        this.color = '#050f2c' // 검정 or 갈색 
      } else if ( this.selectTag === '사랑') {
        this.color = '#ff4f81' // 핑크
      } 
      console.log(this.color)
      this.$emit('changeTag', this.selectTag)
    },
    movieIndex: function (data) {
      this.centerIndex = data
      // console.log(data)
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
    }
  },
  created: function () {
    this.getTagMovies()
    this.$store.dispatch('getMyMovies')
  }
}
</script>

<style>
  .color {
    transition-duration: 2s; 
  }
</style>