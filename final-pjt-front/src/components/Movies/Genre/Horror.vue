<template>
  <div>
    <h1>공포 영화 <img src="@/assets/genreIcons/horror.png" alt="icon" style="height: 3rem;"></h1>
    <ul>
      <li v-for="(movie, idx) in horror" :key="idx">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Horror',
  computed: {
    horror: function () {
      return this.$store.state.movies.horror
    }
  }
}
</script>

<style>

</style>