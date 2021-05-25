<template>
  <div id="MyComments" style="margin-left: 15%; margin-right: 15%;">
    <h1 class="display-3"><i class="el-icon-chat-dot-round"></i> 나의 댓글</h1>
    <br>
    <div class="row row-cols-3 g-4" style="margin-left: 4rem; margin-right: 4rem;">
      <MyCommentCard :comment="comment" v-for="(comment, index) in myComments" :key="index" />
    </div>
  </div>
</template>

<script>
import MyCommentCard from '@/components/Community/Comments/MyCommentCard'

export default {
  name: 'MyComments',
  components: {
    MyCommentCard,
  },
  computed: {
    myComments: function () {
      return this.$store.state.myComments
    }
  },
  created: function () {
    this.$store.dispatch('getMyComments')
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Stylish&display=swap');

#MyComments h1 {
  font-family: 'Black Han Sans', sans-serif;
}

</style>