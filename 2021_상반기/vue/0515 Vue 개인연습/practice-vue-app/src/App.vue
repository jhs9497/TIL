<template>
  
  <div id="app">
    {{ message }}
    <p v-if="seen">나를 볼 수 있어요</p>
      <li 
        :key="todo.id"
        v-for="todo in todos">
        {{ todo.title }}
      </li>
      <input v-model="message">
      <button @click="reverseMessage">메시지 뒤짚기</button>
    <p>
      {{ reverseMsg }}
      {{ now }}
    </p>
    {{ fullName }}
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      message: '안녕하세요 Vue!',
      seen: false ,
      todos: [
        { title: '미진이 바보'},
        { title: '미진이 술쟁이'},
        { title: '바보'},
      ],
      firstName: '윤',
      lastName: '미진',
    }  
  },
  computed: {
    reverseMsg() {
      return this.message.split('').reverse().join('')
    },
    now() {
      return Date.now()
    },
    fullName() {
      return this.firstName + ' ' + this.lastName
    }, 
  },
  methods: {
    reverseMessage() {
      this.message = this.message.split('').reverse().join('')
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
}
</style>
