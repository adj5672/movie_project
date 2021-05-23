<template>
  <div>
    <el-dialog
      title=""
      :visible.sync="$store.state.commentDialogVisible"
      width="90%"
      center>
      <!-- <div class="container" v-if="comment.user">
        <h1>댓글</h1>
        <hr>
        <el-form ref="form" :model="comment" label-width="120px" labelPosition="left">
          <el-form-item label="Content">
            <el-input type="textarea" v-model="comment.content"></el-input>
          </el-form-item>
          <div>생성 시각: {{ comment.created_at }}</div>
          <div>수정 시각: {{ comment.updated_at }}</div>
          <el-button type="primary">수정</el-button>
        </el-form>
        <hr>
        <Comment/>
      </div> -->
      <div class="container">
        <h1>댓글 수정</h1>
        <hr>
        <el-form ref="form" :model="form" label-width="120px" labelPosition="left">
          <el-form-item label="Content">
            <el-input type="textarea" v-model="form.content"></el-input>
          </el-form-item>
          <div>생성 시각: {{ comment.created_at }}</div>
          <div>수정 시각: {{ comment.updated_at }}</div>
          <el-button type="primary">수정</el-button>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CommentDetail',
  data: function () {
    return {
      form: {
        content: null,
      }
    }
  },
  computed: {
    comment: function () {
      return this.$store.state.selectedComment
    },
  },
  updated: function () {
    this.form.content = this.$store.state.selectedComment.content
  }
}
</script>

<style>

</style>