<template>
  <div>
    <el-dialog
      title="Warning"
      :visible.sync="reviewDialogVisible"
      width="30%"
      center>
      <span>It should be noted that the content will not be aligned in center by default</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="reviewDialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="reviewDialogVisible = false">Confirm</el-button>
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