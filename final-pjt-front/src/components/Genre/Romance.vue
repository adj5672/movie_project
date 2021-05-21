<template>
  <div>
    <h3>로맨스 영화</h3>
    <ul>
      <li v-for="(movie, idx) in romance" :key="idx">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Romance',
  computed: {
    romance: function () {
      return this.$store.state.movies.romance
    }
  }
}
</script>

<style>

</style>