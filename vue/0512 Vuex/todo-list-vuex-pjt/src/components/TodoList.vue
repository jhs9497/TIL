<template>
  <div>
    <TodoListItem 
      v-for="(todo, idx) in todos" 
      :key="idx"
      :todo="todo" 
      />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos: function () {
      return this.$store.state.todos // store에 접근하여 todos가져오기
    }
  }
}
</script>

<style>

</style>