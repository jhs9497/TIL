<template>
  <div>
    <transition-group name="list" tag="div">
      <TodoListItem
        v-for="todo in todoList"
        :key="todo.id"
        :todo="todo"
      />
    </transition-group>

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
    todoList() {
      return this.$store.getters.getTodoList
    },
  },
}
</script>

<style>

</style>