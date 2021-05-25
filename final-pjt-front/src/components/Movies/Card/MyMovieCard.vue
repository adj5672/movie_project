<template>

  <div class="col" @click="getDialog" style="padding: 20px; min-width: 196px;">
    <div class="card h-100">
      <img :src="posterSrc" class="card-img-top px-3 pt-3" alt="image">
      <div class="card-body d-flex flex-column justify-content-between">
        <h5 class="card-title fw-bold">{{ movie.title }}</h5>
        <span>{{ movie.release_date }}</span>
      </div>
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Stylish&display=swap');

h5, span {
  font-family: 'Stylish', sans-serif;
}
</style>