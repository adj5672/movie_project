<template>
  <div>
    <h3>공포 영화</h3>
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
      return this.$store.state.horror
    }
  }
}
</script>

<style>

</style>