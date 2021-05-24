<template>
  <img :src="posterSrc" style="height: 100%;" @click="getDialog">
</template>

<script>
export default {
  name: 'TagCarousel',
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