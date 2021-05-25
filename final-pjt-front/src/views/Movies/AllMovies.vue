<template>
  <div class="container" id="AllMovies">
    <Popularity/>
    <Romance/>
    <hr>
    <Action/>
    <hr>
    <Fantasy/>
    <hr>
    <Horror/>
    <hr>
    <Comedy/>
  </div>
</template>

<script>
import Popularity from '@/components/Movies/Popularity'
import Romance from '@/components/Movies/Genre/Romance'
import Action from '@/components/Movies/Genre/Action'
import Fantasy from '@/components/Movies/Genre/Fantasy'
import Horror from '@/components/Movies/Genre/Horror'
import Comedy from '@/components/Movies/Genre/Comedy'

export default {
  name: 'AllMovies',
  components: {
    Popularity,
    Romance,
    Action,
    Fantasy,
    Horror,
    Comedy
  },
  updated: function () {
    this.$store.dispatch('getAllMovies')
  },
  created: function () {
    this.$store.dispatch('getAllMovies')
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

#AllMovies h3 {
  font-family: 'Do Hyeon', sans-serif;
  font-weight: bold;
}
</style>