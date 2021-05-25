<template>
  <div class="back feeling">
    <div class="container">
      <h1 class="feeling fw-bold p-4">오늘의 기분은 어떠신가요?</h1>
      <Recommand/>
    </div>
  </div>
</template>

<script>
import Recommand from '@/components/Movies/Recommand'

export default {
  name: "RecommandMovies",
  components: {
    Recommand,
  },
  computed: {
    backgroundColor: function () {
      return { 'background-color': `${this.$store.state.selectedColor}`}
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Hi+Melody&display=swap');

  .feeling {
    transition-duration: 2s; 
    font-family: 'Hi Melody', cursive;
  }
  
  .back {
    padding-bottom: 200px;
  }
</style>