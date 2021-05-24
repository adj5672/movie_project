<template>
  <div>
    <h3 class="fw-bold my-4"><i class="el-icon-chat-dot-round"></i> 댓글 ({{ $store.state.selectedReview.comment_cnt }})</h3>
    <CreateComment/>
    <CommentList v-for="(comment, idx) in paginatedComments" :key="idx" :comment="comment"/>
    <el-pagination
      class="text-center mt-4"
      background
      :page-size="10"
      layout="prev, pager, next"
      :total="totalPage"
      @current-change="movePage">
    </el-pagination>
  </div>
</template>

<script>
import CreateComment from '@/components/Community/Comments/CreateComment'
import CommentList from '@/components/Community/Comments/CommentList'

export default {
  name: 'Comment',
  components: {
    CreateComment,
    CommentList,
  },
  computed: {
    comments: function () {
      return this.$store.state.selectedReview.comment_set
    },
    paginatedComments: function () {
      const start = (this.page - 1) * 10, // 1페이지면 0~5
            end = start + 10;
      return this.comments.slice(start, end);
    },
    totalPage: function () {
      return this.comments.length
    },
  },
  data: function () {
    return {
      page: 1,
    }
  },
  methods: {
    movePage : function (page) {
      this.page = page
    }
  }
}
</script>

<style>

</style>
