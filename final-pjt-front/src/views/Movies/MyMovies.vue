<template>
  <div>
    <h1>My_Movies</h1>
    <br>
    <p v-for="(movie, idx) in myMovies" :key="idx">{{ movie.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyMovies',
  computed: {
    myMovies: function () {
      return this.$store.state.myMovies
    }
  }
}
</script>

<style>

</style>