<template>
  <div class="container">
    <h1 class="fw-bold">나만의 영화</h1>
    <br>
    <el-row :gutter="24">
      <el-col :span="6" v-for="(movie, index) in myMovies" :key="index" class="my-4">
        <el-card :body-style="{ padding: '10px' }" shadow="hover">
          <MyMovieCard :movie="movie"/>
        </el-card>
      </el-col>
    </el-row>
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
  }
}
</script>

<style>

</style>