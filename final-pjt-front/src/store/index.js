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
    // Login 정보
    isLogin: false,
    config: {},
    // Dialog
    centerDialogVisible: false,
    reviewDialogVisible: false,
    // Movie Detail
    selectedMovie : {},
    selectedReview : {},
    reviews: [],
    // User 정보
    myMovies: [],
  },
  mutations: {
    // 각 알고리즘 별 추천 영화 정보
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
    },

    // 상세 영화 선택 및 상세 영화 리뷰 전체 조회
    SELECT_MOVIE: function (state, movie) {
      state.selectedMovie = movie
    },
    // 상세 리뷰 선택
    SELECT_REVIEW: function (state, review) {
      state.selectedReview = review
    },
    GET_REVIEWS: function (state, reviews) {
      state.reviews = reviews
    },
    // 좋아요 확인 여부
    IS_LIKE: function (state, like) {
      state.selectedMovie = {
        ...state.selectedMovie,
        isLike: like
      }
    },

    // 로그인 및 로그아웃
    LOGIN: function (state, token) {
      state.isLogin = true
      state.config = {
        Authorization: `JWT ${token}`
      }
    },
    LOGOUT: function (state) {
      state.isLogin = false
      state.config = null
    },

    // User가 좋아요를 누른 영화들
    GET_MY_MOVIES: function (state, movies) {
      state.myMovies = movies
    }
  },
  actions: {
    // 전체 영화 정보
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

    // 추천 영화 정보
    getTagMovies: function (context, tag) {
      const tagUrl = `http://127.0.0.1:8000/movies/tag/${tag}`
      axios.get(tagUrl)
        .then(res => {
          context.commit('TAGS', res.data)
        })
        .catch(err => {
          console.log(err)
        })      
    },

    // 상세정보를 확인할 영화 선택
    selectMovie: function (context, movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${movie.id}/`
      })
        .then(res => {
          const merge_data = {
            ...movie,
            ...res.data
          }
          context.commit('SELECT_MOVIE', merge_data)
          context.dispatch('isLike', merge_data)
          context.dispatch('getReviews')
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 상세 영화의 리뷰들 
    getReviews: function (context) {
      const reviewUrl = `http://127.0.0.1:8000/community/${context.state.selectedMovie.id}`
      axios({
        method: 'get',
        url: reviewUrl,
        headers: context.state.config
      })
        .then(res => {
          context.commit('GET_REVIEWS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 상세 영화의 상세 리뷰 
    selectReview: function (context, data) {
      const movie = data[0]
      const review = data[1]
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/community/${movie.id}/review/${review.id}/`,
        headers: context.state.config
      })
        .then(res => {
          context.commit('SELECT_REVIEW', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 상세 영화 좋아요 여부 확인
    isLike: function (context, movie) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${movie.id}/like/`,
        headers: context.state.config
      })
        .then(res => {
          context.commit('IS_LIKE', res.data["isLike"])
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 상세 영화 좋아요 선택
    likeMovie: function (context, movie) {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${movie.id}/like/`,
        headers: context.state.config
      })
        .then(() => {
          context.dispatch('isLike', movie)
        })
        .catch(err => {
          console.log(err)
        })
    },

    // User가 좋아요 누른 영화들 받아오기
    getMyMovies: function (context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/my_movies/`,
        headers: context.state.config
      })
        .then(res => {
          context.commit('GET_MY_MOVIES', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    // 로그인 및 로그아웃
    logIn: function (context, token) {
      context.commit('LOGIN', token)
    },
    logOut: function (context) {
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
