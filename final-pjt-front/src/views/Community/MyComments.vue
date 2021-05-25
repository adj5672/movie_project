<template>
  <div id="MyComments">
    <h1 class="display-3"><i class="el-icon-chat-dot-round"></i> 나의 댓글</h1>
    <br>
    <!-- <el-row :gutter="24">
      <el-col :span="6" v-for="(comment, idx) in myComments" :key="idx" class="my-4">
        <el-card :body-style="{ padding: '10px' }" shadow="hover">
          <MyCommentCard :comment="comment"/>
        </el-card>
      </el-col>
    </el-row> -->
    <div class="row row-cols-4 g-4" style="margin-left: 4rem; margin-right: 4rem;">
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