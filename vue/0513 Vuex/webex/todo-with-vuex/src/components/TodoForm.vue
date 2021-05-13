<template>
  <div>
    <input 
      type="text"
      v-model="userInput"   
      @keyup.enter="onSubmit"
    >
    <button @click="onSubmit">Add</button>
  </div>
</template>

<script>

export default {
  name: 'Todoform',
  data() {
    return {
      userInput: '',
    }
  },
  methods: {
    onSubmit() {
      this.$store.commit('CREATE_TODO', this.newTodo(this.userInput))
    },
    newTodo(content) {
      return {
        id: this.$uuid.v1(),
        content,
        completed: false,
      }
    }
  }
}
</script>

<style>

</style>