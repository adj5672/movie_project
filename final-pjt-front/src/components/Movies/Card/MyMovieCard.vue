<template>
  <div>
    <img :src="posterSrc" class="image" style="width: 100%;" @click="getDialog">
    <div style="padding: 10px;">
        <span class="fw-bold">{{ movie.title }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyMovieCard',
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
    posterSrc: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  },
  methods: {
    getDialog: function () {
      this.$store.state.centerDialogVisible = true
      this.$store.dispatch('selectMovie', this.movie)
    }
  }
}
</script>

<style>

</style>