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
        <TagCarousel :movie="movie" :index="i" :centerIndex="centerIndex"/>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import TagCarousel from '@/components/Movies/Carousel/TagCarousel'

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
    },
    movieIndex: function (data) {
      this.centerIndex = data
      // console.log(data)
    },
  },
  computed: {
    tagMovies: function () {
      return this.$store.state.movies.tag_movies
    },
  },
  created: function () {
    this.getTagMovies()
  }
}
</script>

<style>

</style>