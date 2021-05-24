<template>
  <div>
    <h3>인기 TOP 10</h3>
  <carousel-3d v-if="popularity.length > 0" :display=7 :space=220 :width=210 :height=300 :controls-visible="true" @after-slide-change="movieIndex">
    <slide v-for="(movie, i) in popularity" :index="i" :key="i" class="rounded-3">
      <PopularityCarousel :movie="movie" :index="i" :centerIndex="centerIndex"/>
    </slide>
  </carousel-3d>
  </div>
</template>

<script>
import PopularityCarousel from '@/components/Movies/Carousel/PopularityCarousel'

export default {
  name: 'Popularity',
  components: {
    PopularityCarousel
  },
  computed: {
    popularity: function () {
      return this.$store.state.movies.popularity
    }
  },
  data: function () {
    return {
      centerIndex: 0,
    }
  },
  methods: {
    movieIndex: function (data) {
      this.centerIndex = data
      // console.log(data)
    },
  }
}
</script>

<style>

</style>