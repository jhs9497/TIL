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
import { mapState } from 'vuex' // mapState 메소드만 쓰겠다.
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos // store에 접근하여 todos가져오기
    // }
    ...mapState([ // State랑 연결하기 위해서 mapState를 사용, 위에 this.$store.state.todos의 todos를 가져옴!
      'todos',
    ])
  }
}
</script>

<style>

</style>