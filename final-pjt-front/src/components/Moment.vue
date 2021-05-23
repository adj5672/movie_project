<template>
  <div>
    <h3>{{ $store.state.Year }} . {{ $store.state.Month }} . {{ $store.state.Day }}</h3>
    <p>
      <i class="el-icon-time h1"></i> 
      <span class="h1"> {{ $store.state.Hour }}</span>
      <span class="h1"> : </span>
      <span class="h1">{{ $store.state.Minute }}</span>
      <span> {{ $store.state.Second }}</span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'Moment',
}
</script>

<style>

</style>