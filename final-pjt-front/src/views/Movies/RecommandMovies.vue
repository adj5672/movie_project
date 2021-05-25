<template>
  <div class="back feeling" style="margin-left: 15%; margin-right: 15%;">
    <h1 class="feeling fw-bold p-4 display-3">오늘의 <span class="feeling display-3 fw-bold text-danger">기분</span>은 어떠신가요?</h1>
    <Recommand/>
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
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

  .feeling {
    transition-duration: 2s; 
    /* font-family: 'Hi Melody', cursive; */
    font-family: 'Jua', sans-serif;
  }
  
  .back {
    padding-bottom: 100px;
  }
</style>