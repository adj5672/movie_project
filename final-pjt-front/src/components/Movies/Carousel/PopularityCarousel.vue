<template>
  <div style="height: 100%;">
    <img :src="posterSrc" style="height: 100%;" @click="getDialog">
    <img :src="numberSrc" alt="number" class="btn position-absolute bottom-0 start-0" style="height: 30%; width: auto;">
  </div>
</template>

<script>
export default {
  name: 'PopularityCarousel',
  props: {
    movie: {
      type: Object
    },
    index: {
      type: Number
    },
    centerIndex: {
      type: Number
    }
  },
  computed: {
    posterSrc: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
    numberSrc: function () {
      return require(`@/assets/numberLogos/${this.index+1}.png`)
    }
  },
  methods: {
    getDialog: function () {
      if (this.centerIndex === this.index) {
        this.$store.state.centerDialogVisible = true
        this.$store.dispatch('selectMovie', this.movie)
      }
      this.$emit('movie-index', this.index)
    }
  }
}
</script>

<style>

</style>