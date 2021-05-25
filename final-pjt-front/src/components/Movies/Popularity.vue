<template>
  <div style="margin-bottom: 5rem;">
    <h3 class="my-auto">인기 TOP 10</h3>
    <carousel-3d v-if="popularity.length" :display=7 :space=220 :width=210 :height=300 :controls-visible="true" @after-slide-change="movieIndex">
      <slide v-for="(movie, i) in popularity" :index="i" :key="i" class="rounded-3 border">
        <div class="position-relative">
          <PopularityCarousel style="cursor: pointer" :movie="movie" :index="i" :centerIndex="centerIndex"/>
          <button class="btn position-absolute top-0 end-0" :style="heartVisible(movie)"><font-awesome-icon style="color:crimson;" :icon="['fas','heart']"/></button>
        </div>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import PopularityCarousel from '@/components/Movies/Carousel/PopularityCarousel'
import _ from 'lodash'

export default {
  name: 'Popularity',
  components: {
    PopularityCarousel
  },
  computed: {
    popularity: function () {
      return this.$store.state.movies.popularity
    },
    myMovies: function () {
      return this.$store.state.myMovies
    },
  },
  data: function () {
    return {
      centerIndex: 0,
    }
  },
  methods: {
    movieIndex: function (data) {
      this.centerIndex = data
      // console.log(data)
    },
    heartVisible: function (movie) {
      var tmp = 0
      _.forEach((this.myMovies), function(myMovie) {
        if (movie.id === myMovie.id) {
          tmp = 1
        }
      })
      if (tmp === 1) {
        return { visibility: 'visible' }
      } else {
        return { visibility: 'hidden' }
      }
    }
  },
  created: function () {
    this.$store.dispatch('getMyMovies')
    // console.log(this.$store.state.myMovies)
  }
  
}
</script>

<style>

</style>