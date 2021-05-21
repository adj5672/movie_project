<template>
  <div class="container">
    <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
      Login
    </el-button>

    <el-drawer
      title="I am the title"
      :visible.sync="drawer"
      :with-header="false">
      <span>Hi there!</span>
    </el-drawer>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  data: function () {
    return {
      drawer: false,
    }
  }
}
</script>

<style>

</style>