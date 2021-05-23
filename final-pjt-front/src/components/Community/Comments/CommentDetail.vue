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
        <el-form ref="form" :model="comment" label-width="120px" labelPosition="left">
          <el-form-item label="Content">
            <el-input type="textarea" v-model="comment.content"></el-input>
          </el-form-item>
          <div>생성 시각: {{ createdAt }}</div>
          <div>수정 시각: {{ updatedAt }}</div>
          <el-button @click="updateComment" type="primary">수정</el-button>
        </el-form>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CommentDetail',
  computed: {
    comment: function () {
      return this.$store.state.selectedComment
    },
    createdAt: function () {
      return this.$moment(this.comment.created_at).format('YY-MM-DD HH:mm:ss')
    },
    updatedAt: function () {
      return this.$moment(this.comment.updated_at).format('YY-MM-DD HH:mm:ss')
    },

  },
  methods: {
    updateComment: function () {
      this.$store.state.commentDialogVisible = false
    }
  }
  
}
</script>

<style>

</style>