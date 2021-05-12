<template>
  <div>
    <input type="text" v-model="todoTitle" @keyup.enter="createTodo"> 
    <button @click="createTodo">할 일 추가!</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '', // v-model로 연결된 인풋값 들어옴
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = { // django context처럼 만들어주기
        title: this.todoTitle,
        completed: false,
      }
      if (todoItem.title.trim()) {
        this.$store.dispatch('createTodo', todoItem) // action 호출
      }
      this.todoTitle = '' // 보낸 후 data 초기화
    }
  }
}
</script>

<style>

</style>