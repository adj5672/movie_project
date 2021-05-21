<template>
  <div>
    <h3>인기 TOP 10</h3>
  <carousel-3d>
    <slide v-for="(movie, i) in popularity" :index="i" :key="i">
      <PopularityCarousel :movie="movie" :index="i"/>
    </slide>
</carousel-3d>
  </div>
</template>

<script>
import PopularityCarousel from '@/components/Carousel/PopularityCarousel'

export default {
  name: 'Popularity',
  components: {
    PopularityCarousel
  },
  computed: {
    popularity: function () {
      return this.$store.state.popularity
    }
  }
}
</script>

<style>

</style>