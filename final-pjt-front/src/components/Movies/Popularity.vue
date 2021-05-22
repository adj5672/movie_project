<template>
  <div>
    <h3>인기 TOP 10</h3>
  <carousel-3d v-if="popularity.length === 10">
    <slide v-for="(movie, i) in popularity" :index="i" :key="i" class="rounded-3">
      <PopularityCarousel :movie="movie" :index="i" :centerIndex="centerIndex" @movie-index="movieIndex"/>
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
    movieIndex: function (index) {
      this.centerIndex = index
    }
  }
}
</script>

<style>

</style>