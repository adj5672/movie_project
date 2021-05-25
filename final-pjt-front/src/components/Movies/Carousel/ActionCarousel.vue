<template>
  <div class="box" @click="getDialog" style="height: 100%;">
    <img class="image" :src="posterSrc" style="height: 100%;" @error="defaultImage">
    <div class="overlay">
      <div class="title">{{ movie.title }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ActionCarousel',
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
    background-color: #eeee;
  }

  .title {
    color: black;
    font: bold;
    font-size: 25px;
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }

  .box:hover .overlay {
    opacity: 0.9;
  }

</style>