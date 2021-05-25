<template>
  <div style="height: 100%;">
    <img :src="posterSrc" style="height: 100%;" @click="getDialog" @error="defaultImage">
  </div>
</template>

<script>
export default {
  name: 'ComedyCarousel',
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
  },
  methods: {
    getDialog: function () {
      if (this.centerIndex === this.index) {
        this.$store.state.centerDialogVisible = true
        this.$store.dispatch('selectMovie', this.movie)
      }
      this.$emit('movie-index', this.index)
    },
    defaultImage: function (event) {
      event.target.src = this.defaultSrc
    }
  },
  data: function () {
    return {
      defaultSrc: require("@/assets/default.png")
    }
  }
}
</script>

<style>

</style>