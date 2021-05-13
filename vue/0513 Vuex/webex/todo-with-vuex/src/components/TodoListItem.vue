<template>
  <div>
    <input @click="onClick" type="checkbox" v-model="todo.completed">
    <span :class="{ completed : todo.completed }">{{ todo.content }}</span>
    <button @click="onDelete">삭제</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onClick() {
      // 1. mutation 호출 
      this.$store.commit('UPDATE_TODO', this.todo)
      // 2. store에서 todo의 completd 값 변경
    },
    onDelete() {
      this.$store.commit('DELETE_TODO', this.todo)
    }
  },
}
</script>

<style scoped>
  .completed{
    text-decoration: line-through;
    color: red;
  }
</style>