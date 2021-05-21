<template>
  <div>
    <h3>판타지 영화</h3>
    <ul>
      <li v-for="(movie, idx) in fantasy" :key="idx">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Fantasy',
  computed: {
    fantasy: function () {
      return this.$store.state.movies.fantasy
    }
  }
}
</script>

<style>

</style>