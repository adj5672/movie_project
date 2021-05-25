<template>
  <div id="MyMovies" style="margin-left: 15%; margin-right: 15%;">
    <h1 class="display-3"><i class="el-icon-video-camera-solid"></i> 나만의 영화</h1>
    <br>
    <div class="row row-cols-4 g-4" style="margin-left: 4rem; margin-right: 4rem;">
      <MyMovieCard :movie="movie" v-for="(movie, index) in myMovies" :key="index" />
    </div>
  </div>
</template>

<script>
import MyMovieCard from '@/components/Movies/Card/MyMovieCard'

export default {
  name: 'MyMovies',
  computed: {
    myMovies: function () {
      return this.$store.state.myMovies
    }
  },
  components: {
    MyMovieCard,
  },
  created: function () {
    this.$store.dispatch('getMyMovies')
    // console.log(this.$store.state.myMovies)
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Stylish&display=swap');

#MyMovies h1 {
  font-family: 'Black Han Sans', sans-serif;
}

</style>