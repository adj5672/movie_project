import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: {
      popularity: [],
      romance: [],
      action: [],
      fantasy: [],
      horror: [],
      comedy: [],
      tag_movies: [],
    },
    isLogin: false,
  },
  mutations: {
    POPULARITY: function (state, movies) {
      state.movies.popularity = movies
    }, 
    ROMANCE: function (state, movies) {
      state.movies.romance = movies
    }, 
    ACTION: function (state, movies) {
      state.movies.action = movies
    }, 
    FANTASY: function (state, movies) {
      state.movies.fantasy = movies
    }, 
    HORROR: function (state, movies) {
      state.movies.horror = movies
    }, 
    COMEDY: function (state, movies) {
      state.movies.comedy = movies
    },
    TAGS: function (state, movies) {
      state.movies.tag_movies = movies
    } 
  },
  actions: {
    getAllMovies: function (context) {

      // Top 10
      const popularityUrl = 'http://127.0.0.1:8000/movies/popularity/'
      axios.get(popularityUrl)
        .then(res => {
          context.commit('POPULARITY', res.data)
        })
        .catch(err => {
          console.log(err)
        })
        
      // Romance
      const romanceUrl = 'http://127.0.0.1:8000/movies/genre/10749/'
      axios.get(romanceUrl)
        .then(res => {
          context.commit('ROMANCE', res.data)
        })
        .catch(err => {
          console.log(err)
        })

      // Action
      const actionUrl = 'http://127.0.0.1:8000/movies/genre/28/'
      axios.get(actionUrl)
        .then(res => {
          context.commit('ACTION', res.data)
        })
        .catch(err => {
          console.log(err)
        })

      // Fantasy
      const fantasyUrl = 'http://127.0.0.1:8000/movies/genre/14/'
      axios.get(fantasyUrl)
        .then(res => {
          context.commit('FANTASY', res.data)
        })
        .catch(err => {
          console.log(err)
        })

      // Horror
      const HorrorUrl = 'http://127.0.0.1:8000/movies/genre/27/'
      axios.get(HorrorUrl)
        .then(res => {
          context.commit('HORROR', res.data)
        })
        .catch(err => {
          console.log(err)
        })
        
      // Comedy
      const comedyUrl = 'http://127.0.0.1:8000/movies/genre/35/'
      axios.get(comedyUrl)
        .then(res => {
          context.commit('COMEDY', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    getTagMovies: function (context, tag) {
      console.log(context, tag)
      const tagUrl = `http://127.0.0.1:8000/movies/tag/${tag}`
      axios.get(tagUrl)
        .then(res => {
          context.commit('TAGS', res.data)
        })
        .catch(err => {
          console.log(err)
        })      
    }
  },
  modules: {
  }
})
