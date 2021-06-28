<template>
  <div>
    <h1>Child</h1>
    <button @click="onClick">부모님 들리시나용</button>
  </div>
</template>

<script>
export default {
  name: 'Child',
  methods:{
    onClick: function() {
      this.$emit('my-event')
    },
  },
}
</script>

<style>

</style>