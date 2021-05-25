<template>
  <div class="container">
    <h1 class="feeling" :style="backgroundColor">오늘의 기분은 어떠신가요?</h1>
    <Recommand @changeTag="changeTag"/>
  </div>
</template>

<script>
import Recommand from '@/components/Movies/Recommand'

export default {
  name: "RecommandMovies",
  data: function () {
    return {
      backgroundColor: {},
    }
  },
  components: {
    Recommand,
  },
  methods: {
    changeTag: function (tag) {
      if (tag === '기쁨') {
        this.backgroundColor = { 'color' : '#ffc168'} // 노랑
      } else if ( tag === '슬픔') {
        this.backgroundColor = { 'color' : '#8e43e7' } // 보라
      } else if ( tag === '짜증') {
        this.backgroundColor = { 'color' : '#b84592' } // 빨강
      } else if ( tag === '심심') {
        this.backgroundColor = { 'color' : '#050f2c' } // 검정 or 갈색 
      } else if ( tag === '사랑') {
        this.backgroundColor = { 'color' : '#ff4f81' } // 핑크
      } 
    }
  }
}
</script>

<style>
  .feeling {
    transition-duration: 2s; 
  }
</style>