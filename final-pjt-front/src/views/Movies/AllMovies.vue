<template>
  <div>
    <div id="AllMovies" style="margin-left: 15%; margin-right: 15%;">
    <Popularity/>
    <Romance/>
    <Action/>
    <Fantasy/>
    <Horror/>
    <Comedy/>
    </div>
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
  created: function () {
    this.$store.dispatch('getAllMovies')
  },
  computed: {
    backgroundColor: function () {
      return { 'background-color': `${this.$store.state.selectedColor}`}
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap');

#AllMovies h1 {
  font-family: 'Do Hyeon', sans-serif;
  font-weight: bold;
}
</style>