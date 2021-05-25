<template>
  <div>
    <h1>액션 영화 <img src="@/assets/genreIcons/action.png" alt="icon" style="height: 3rem;"></h1>
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