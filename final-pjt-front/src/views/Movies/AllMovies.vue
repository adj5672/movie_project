<template>
  <div class="container">
    <h1>전체영화</h1>
    <hr>
    <Popularity/>
    <hr>
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
  created: function () {
    this.$store.dispatch('getAllMovies')
  }
}
</script>

<style>

</style>