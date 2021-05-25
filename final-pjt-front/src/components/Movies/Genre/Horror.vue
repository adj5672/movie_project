<template>
  <div style="margin-bottom: 5rem;">
    <h1>공포 영화 <img src="@/assets/genreIcons/horror.png" alt="icon" style="height: 3rem;"></h1>
    <carousel-3d v-if="horror.length" class="my-auto" :autoplay=true :autoplayTimeout=5000 :display=7 :space=280 :width=245 :height=350 :controls-visible="true" @after-slide-change="movieIndex">
      <slide v-for="(movie, i) in horror" :index="i" :key="i" class="rounded-3 border">
        <div class="position-relative" style="height: 100%;">
          <HorrorCarousel style="cursor: pointer" :movie="movie" :index="i" :centerIndex="centerIndex" @updateMyMovies="updateMyMovies"/>
          <button class="btn position-absolute top-0 end-0" :style="heartVisible(movie)"><font-awesome-icon size="lg" style="color:crimson;" :icon="['fas','heart']"/></button>
        </div>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import HorrorCarousel from '@/components/Movies/Carousel/HorrorCarousel'
import _ from 'lodash'

export default {
  name: 'Horror',
  components: {
    HorrorCarousel
  },
  computed: {
    horror: function () {
      return this.$store.state.movies.horror
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
    },
    updateMyMovies: function () {
      this.$store.dispatch('getMyMovies')
    },
  },
  created: function () {
    this.$store.dispatch('getMyMovies')
  },
}
</script>

<style>

</style>