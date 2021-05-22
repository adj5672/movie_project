<template>
  <div>
    <el-dialog
      title="Warning"
      :visible.sync="$store.state.reviewDialogVisible"
      width="90%"
      center>
      <span>It should be noted that the content will not be aligned in center by default</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="$store.state.reviewDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="$store.state.reviewDialogVisible = false">Confirm</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'ReviewDetail',
}
</script>

<style>

</style>