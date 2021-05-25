<template>
  <div>
    <h3>코메디 영화 <img src="@/assets/genreIcons/comedy.png" alt="icon" style="height: 2rem;"></h3>
    <ul>
      <li v-for="(movie, idx) in comedy" :key="idx">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Comedy',
  computed: {
    comedy: function () {
      return this.$store.state.movies.comedy
    }
  }
}
</script>

<style>

</style>