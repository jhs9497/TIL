<template>
  <div>
    <span 
      @click="updateTodo(todo)"  
      :class="{ completed: todo.completed }" 
    >{{ todo.title }}</span> 
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo:{
      type: Object,
    }
  },
  methods: {
    // deleteTodo: function () {
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodo: function () {
    //   this.$store.dispatch('updateTodo', this.todo)
    // },
    ...mapActions([  // 근데 this.todo도 넘겨줘야 하기 때문에 위에 click시 updateTodo 호출할때 같이 넣어서 보내준다
      'deleteTodo',
      'updateTodo',
    ])
  },
}
</script>

<style scoped>
  .completed { 
    /* class가 completed인 곳에만 취소선을 넣겠다 */
    text-decoration: line-through;
  }

</style>