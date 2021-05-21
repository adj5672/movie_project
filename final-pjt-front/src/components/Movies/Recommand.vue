<template>
  <div>
    <select id="tag_select" v-model="selectTag">
      <option value="기쁨">기쁨</option>
      <option value="슬픔">슬픔</option>
      <option value="짜증">짜증</option>
      <option value="심심">심심</option>
      <option value="사랑">사랑</option>
    </select>
    <button @click="getTagMovies">선택</button>
    <carousel-3d>
      <slide v-for="(movie, i) in tagMovies" :index="i" :key="i">
        <TagCarousel :movie="movie" :index="i"/>
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
    }
  },
  components: {
    TagCarousel
  },
  methods: {
    getTagMovies: function () {
      this.$store.dispatch('getTagMovies', this.selectTag)
    }
  },
  computed: {
    tagMovies: function () {
      return this.$store.state.movies.tag_movies
    }
  }
}
</script>

<style>

</style>