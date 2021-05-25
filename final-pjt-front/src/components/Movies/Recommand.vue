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
      <el-button @click="getTagMovies" type="primary">선택</el-button>
    </div>
    <carousel-3d v-if="$store.state.movies.tag_movies.length" :display=7 :space=250 :width=280 :height=400 :controls-visible="true" @after-slide-change="movieIndex">
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

export default {
  name: 'Recommand',
  data: function () {
    return {
      selectTag: '기쁨',
      centerIndex: 0,
    }
  },
  components: {
    TagCarousel
  },
  methods: {
    getTagMovies: function () {
      this.$store.dispatch('getTagMovies', this.selectTag)
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
    changeTag: function () {
      this.$emit('changeTag', this.selectTag)
    }
  },
  computed: {
    tagMovies: function () {
      return this.$store.state.movies.tag_movies
    },
    myMovies: function () {
      return this.$store.state.myMovies
    }
  },
  created: function () {
    this.getTagMovies()
    this.$store.dispatch('getMyMovies')
  }
}
</script>

<style>

</style>