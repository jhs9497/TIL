<template>
  <div id="app" class='container'>
    <TodoForm/>
    <div v-if="errorMsg"
      class="alert alert-danger my-2" 
      role="alert"
    >
      {{ errorMsg }}
    </div>
    <TodoList/>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    errorMsg() {
      return this.$store.state.errorMsg
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  max-width: 500px;
}
</style>
