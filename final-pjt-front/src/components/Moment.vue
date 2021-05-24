<template>
  <div>
    <div class="text-end" style="width: 90%;">
      <img src="@/assets/clock.png" alt="clock" class="w-25">
    </div>
    <div class="border rounded-3 p-3">
      <h3 class="fw-bold">{{ $store.state.Year }} . {{ $store.state.Month }} . {{ $store.state.Day }}</h3>
      <p class="my-auto">
        <i class="el-icon-time display-5 fw-bold"></i> 
        <span class="display-5 fw-bold"> {{ $store.state.Hour }}</span>
        <span class="display-5 fw-bold"> : </span>
        <span class="display-5 fw-bold">{{ $store.state.Minute }}</span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Moment',
}
</script>

<style scoped>

</style>