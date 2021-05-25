<template>
  <div>
    <h3>공포 영화 <img src="@/assets/genreIcons/horror.png" alt="icon" style="height: 2rem;"></h3>
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