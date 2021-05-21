<template>
  <img :src="posterSrc" style="height: 100%;">
</template>

<script>
export default {
  name: 'PopularityCarousel',
  props: {
    movie: {
      type: Object
    },
  },
  computed: {
    posterSrc: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  }
}
</script>

<style>

</style>