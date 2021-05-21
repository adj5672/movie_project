<template>
  <div>
    <h3>액션 영화</h3>
    <ul>
      <li v-for="(movie, idx) in action" :key="idx">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Action',
  computed: {
    action: function () {
      return this.$store.state.movies.action
    }
  }
}
</script>

<style>

</style>