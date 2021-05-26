<template>
  <div class="box" @click="getDialog" style="height: 100%;">
    <img class="image" :src="posterSrc" style="height: 100%;" @error="defaultImage">
    <img :src="numberSrc" alt="number" class="btn position-absolute bottom-0 start-0" style="height: 30%; width: auto;">
    <div class="overlay">
      <div class="title SansBold">{{ movie.title }}</div>
      <div class="genres"><span v-for="(genre, idx) in movie.genres" :key="idx" class="Jua fw-bold me-2">#{{ genre.name }}</span></div>
      <div class="Jua release_date">{{ movie.release_date }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PopularityCarousel',
  props: {
    movie: {
      type: Object
    },
    index: {
      type: Number
    },
    centerIndex: {
      type: Number
    }
  },
  computed: {
    posterSrc: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
    numberSrc: function () {
      return require(`@/assets/numberLogos/${this.index+1}.png`)
    }
  },
  methods: {
    getDialog: function () {
      if (this.centerIndex === this.index) {
        this.$store.state.centerDialogVisible = true
        this.$store.dispatch('selectMovie', this.movie)
      }
      this.$emit('movie-index', this.index)
    },
    defaultImage: function (event) {
      event.target.src = this.defaultSrc
    }
  },
  data: function () {
    return {
      defaultSrc: require("@/assets/default.png")
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

  .box {
    position: relative;

  }
  .overlay {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    height: 100%;
    width: 100%;
    opacity: 0;
    transition: .3s ease;
    background-color: lightgray;
  }

  .title {
    color: black;
    font-weight: bold;
    width: 90%;
    font-size: 36px;
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .genres {
    font-size: 22px;
    position: absolute;
    color:royalblue;
    top: 60%;
    left: 50%;
    width: 90%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .release_date {
    color: black;
    font-size: 20px;
    position: absolute;
    top: 80%;
    left: 50%;
    width: 90%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .box:hover .overlay {
    opacity: 0.8;
  }
  .Sans {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 400;
  }

  .SansBold {
    font-family: 'Noto Sans KR', sans-serif;
    font-weight: 900;
  }

  .Jua {
    font-family: 'Jua', sans-serif;
  }
</style>