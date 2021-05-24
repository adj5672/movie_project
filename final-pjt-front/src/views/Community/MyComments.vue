<template>
  <div class="container">
    <h1 class="fw-bold">나의 댓글</h1>
    <hr>
    <el-row :gutter="24">
      <el-col :span="6" v-for="(comment, idx) in myComments" :key="idx" class="my-4">
        <el-card :body-style="{ padding: '10px' }" shadow="hover">
          <MyCommentCard :comment="comment"/>
        </el-card>
      </el-col>
    </el-row>
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

</style>