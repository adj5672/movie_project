<template>
  <div class="col" @click="getDialog" style="padding: 20px; min-width: 196px;">
    <div class="card card-hover h-100 shadow" style="cursor: pointer;">
      <img :src="posterSrc" class="card-img-top px-3 pt-3" alt="image">
      <div class="card-body d-flex flex-column justify-content-between align-items-center">
        <h5 class="card-title fw-bold mb-1">{{ movie.title }}</h5>
        <div class="d-flex flex-wrap w-100 justify-content-center">
          <span v-for="(genre, idx) in movie.genres" :key="idx" class="mx-1 text-primary">#{{ genre.name }} </span>
        </div>
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
  data: function () {
    return {
      mouseover: false
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
    },
    mouseOver: function () {
      this.mouseover = true
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